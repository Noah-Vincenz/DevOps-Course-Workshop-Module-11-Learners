# Workshop Module 11

This repository is for learners on Corndel's DevOps apprenticeship.

During workshop 11 you'll be following the instructions in [during_workshop_11.md](during_workshop_11.md).

## Pre-requisites

You should have received an email inviting you to the "Softwire Academy" Azure directory. Please accept the invitation.

You need to have an Azure account. You can create a free account [here](https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F).

Also, make sure you have installed the following:

* [Visual Studio Code](https://code.visualstudio.com/download)
* [Git](https://git-scm.com/)
* [.NET 5.0 SDK](https://dotnet.microsoft.com/download)
* [Azure Functions Core Tools version 3.x.](https://docs.microsoft.com/en-gb/azure/azure-functions/functions-run-local#v2)
* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
* [Python](https://www.python.org/downloads/)
  * Version 3.6 or up; check this by running `python --version`
* [Postman](https://www.postman.com/downloads/)


### My Notes

This project runs two hosted functions (FaaS) in the Azure Cloud platform. There is an endpoint listening to POST requests to 'http://localhost:7071/api/HttpEndpoint' containing the following body:
```
{
    "subtitle": "It was a bright cold day in April, and the clocks were striking thirteen.",
    "languages": ["it", "de"]
}
```
Once the function is deployed/hosted in the Azure cloud this can be accessed via 'https://<APP_NAME>.azurewebsites.net/api/httpendpoint'.

The first function (located in HttpEndpoint) stores the input in the 'AcmeTranslations' table in the Azure cloud and sends a message to the 'acmesub-translations-queue' for each language element in the input list. The second function (located in TranslatorEndpoint) then processes each message by querying the corresponding entry in the 'AcmeTranslations' table, translating the input/subtitle in that table entry to the target language (ie. 'de'), and creating a new table entry with the translated output in the 'AcmeTranslations2' table in the Azure cloud. Currently the translation funciton only converts the text to uppercase letters, but optional functionality to include Azure Translator has been included.

To fetch changes from the remote cloud run the following:
```
func azure functionapp fetch-app-settings <APP_NAME>
```

To run a function locally run the following:
```
func start
```
inside the 'AcmeSubProject' directory.