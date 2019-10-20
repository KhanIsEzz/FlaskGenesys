#start webapp
question = '"Whats the best restaurant in Toronto?"'

#get answer
#generate token
import requests
URL = "https://api.genesysappliedresearch.com/v2/knowledge/generatetoken"
response = requests.post(url = URL, headers={'Accept':'*/*','cache-control':'no-cache','organizationid':'be64cce3-44f8-4cd5-9e12-dbfed265165c','secretkey':'0845a386-ab66-4fe8-a1cb-56ef34a3b658'})
jsonResponse = response.json()
token = jsonResponse['token']
#now get response
DATA = '{"query":'+question+',"pageSize": 1,"pageNumber": 1,"sortOrder": "string","sortBy": "string","languageCode":"en-US","documentType": "Faq","model":"b4c48bc5-0893-44a5-b9e9-c6975b3b888a"}'
response = requests.post(url = 'https://api.genesysappliedresearch.com/v2/knowledge/knowledgebases/7613d1f7-09a7-41f5-a0ba-94f7f6d91d2f/search', data = DATA, headers = {'token':token,'accept':'application/json','Content-Type':'application/json','organizationid':'be64cce3-44f8-4cd5-9e12-dbfed265165c'})
jsonResponse = response.json()
results = jsonResponse['results'][0]
restaurants = results['faq']['answer']
print(restaurants)

#if it's not a rating based question:
if (restaurants[0] == 'g'):

#

#get best customer reviews

#update client view
