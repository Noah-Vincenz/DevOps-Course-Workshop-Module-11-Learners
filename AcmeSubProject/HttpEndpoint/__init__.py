import logging
import azure.functions as func
import uuid
import json
import typing

def main(req: func.HttpRequest, tableMessage: func.Out[str], queueMessage: func.Out[typing.List[str]]) -> func.HttpResponse:
    logging.info('HTTP trigger function received a request.')

    req_body = req.get_json()
    subtitle = req_body.get('subtitle')
    languages = req_body.get('languages')

    rowKey = str(uuid.uuid4())

    data = {
        "Name": "A subtitle translation",
        "PartitionKey": "subtitles",
        "RowKey": rowKey,
        "translation": subtitle
    }

    tableMessage.set(json.dumps(data))

    queue_data = []

    for lang in languages:
        queue_data.append(
            json.dumps(
                {
                    "rowKey": rowKey,
                    "languageCode": lang
                }
            )
        )
    queueMessage.set(queue_data)

    return func.HttpResponse(
        f"Table entry created with the rowKey: {rowKey} and sent translations to queue",
        status_code = 200
    )
