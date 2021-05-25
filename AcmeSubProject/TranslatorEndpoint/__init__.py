import logging
import json
import azure.functions as func
import uuid
import requests, uuid, json

def main(msg: func.QueueMessage, tableInMessage, tableOutMessage: func.Out[str]):
    logging.info('Python queue trigger function processed a queue item.')

    table_data = json.loads(tableInMessage)
    translation = table_data['translation']

    result = json.dumps({
        'id': msg.id,
        'body': msg.get_body().decode('utf-8'),
        'expiration_time': (msg.expiration_time.isoformat()
                            if msg.expiration_time else None),
        'insertion_time': (msg.insertion_time.isoformat()
                           if msg.insertion_time else None),
        'time_next_visible': (msg.time_next_visible.isoformat()
                              if msg.time_next_visible else None),
        'pop_receipt': msg.pop_receipt,
        'dequeue_count': msg.dequeue_count,
    })

    logging.info(result)

    # TRANSLATE TEXT USING AZURE TRANSLATOR
    # subscription_key = "YOUR_SUBSCRIPTION_KEY"
    # endpoint = "https://api.cognitive.microsofttranslator.com/"
    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    # location = "YOUR_RESOURCE_LOCATION"
    # path = '/translate'
    # constructed_url = endpoint + path
    # params = {
    #     'api-version': '3.0',
    #     'from': 'en',
    #     'to': msg.get_json()['languageCode']
    # }
    # constructed_url = endpoint + path
    # headers = {
    #     'Ocp-Apim-Subscription-Key': subscription_key,
    #     # 'Ocp-Apim-Subscription-Region': location,
    #     'Content-type': 'application/json',
    #     'X-ClientTraceId': str(uuid.uuid4())
    # }
    # # You can pass more than one object in body.
    # body = [{
    #     'text': translation
    # }]
    # request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # response = request.json()
    # translation_object = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))[0]['translations']
    # translated_text = translation_object[0]['text']

    # just converting to upper case
    translated_text = translation.upper()

    tableOutMessage.set(json.dumps(
        {
            "Name": "A subtitle translation",
            "PartitionKey": "subtitles",
            "RowKey": str(uuid.uuid4()),
            "translation": translation.upper(),
            "language": msg.get_json()['languageCode']
        }
    ))