from surls import app
import requests

apiKey = app.config['DB_API_KEY']
dbName = app.config['DB_NAME']
collection = app.config['DB_COLLECTION']
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def get(id):
    url = 'https://api.mongolab.com/api/1/databases/{}/collections/{}/{}?apiKey={}' \
        .format(dbName, collection, id, apiKey)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 404:
        response.raise_for_status()
    return response.json()


def add(model):
    url = 'https://api.mongolab.com/api/1/databases/{}/collections/{}?apiKey={}'. \
        format(dbName, collection, apiKey)
    payload = model.to_json()
    response = requests.post(url=url, data=payload, headers=headers)
    return response
