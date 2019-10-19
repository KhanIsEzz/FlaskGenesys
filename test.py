import requests
URL = "https://api.genesysappliedresearch.com/v2/knowledge/generatetoken"
response = requests.post(url = URL, headers={'Accept':'*/*','cache-control':'no-cache','organizationid':'be64cce3-44f8-4cd5-9e12-dbfed265165c','secretkey':'0845a386-ab66-4fe8-a1cb-56ef34a3b658'})
jsonResponse = response.json()
print(jsonResponse)

