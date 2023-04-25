from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

API_KEY = '8899a961af34415a95a22801d6a0dd89'
# API_KEY = '8149199a9dbb4cefb3e460a897ee6273'
ENDPOINT = 'https://resume-api.cognitiveservices.azure.com/'
# ENDPOINT = 'https://nikhil.cognitiveservices.azure.com/'

def client():
    try:
        client = TextAnalyticsClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(API_KEY)
        )
        return client
    except Exception as e:
        print(e)
        