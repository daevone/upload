from mayan_api_client import API

api = API(host='http://192.168.22.188:81', username='Dave', password='dbvjdu123')

for result in api.metadata.metadata_types.get()['results']:
   print(result['name'])

'''for result in api.documents.document_types.get()['results']:
    print(result['label'])
'''