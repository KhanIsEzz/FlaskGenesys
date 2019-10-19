#start webapp
import cgi
form = cgi.FieldStorage()
searchterm = form.getvalue('search')
question = searchterm 
print(question)

#get answer
import requests

URL = "https://api.genesysappliedresearch.com/v2/knowledge/generatetoken"
response = requests.post(url = URL, headers={'Accept':'*/*','cache-control':'no-cache','organizationid':'be64cce3-44f8-4cd5-9e12-dbfed265165c','secretkey':'0845a386-ab66-4fe8-a1cb-56ef34a3b658'})
jsonResponse = response.json()
token = jsonResponse['token']
#now get response
response = requests.post(url = 'https://api.genesysappliedresearch.com/v2/knowledge/knowledgebases/7613d1f7-09a7-41f5-a0ba-94f7f6d91d2f/search', data = '{"query":'+question+',"pageSize": 5,"pageNumber": 1,"sortOrder": "string","sortBy": "string","languageCode":"en-US","documentType": "Faq"}', headers = {'token':token})
jsonResponse = response.json()
print(token)
print(jsonResponse)

#get best customer reviews

#update client view
