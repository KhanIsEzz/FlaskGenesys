from flask import Flask, render_template,request
import requests

app = Flask(__name__)
@app.route('/')
def home():
    print("lol")
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['search']
    question=text
    URL = "https://api.genesysappliedresearch.com/v2/knowledge/generatetoken"
    response = requests.post(url = URL, headers={'Accept':'*/*','cache-control':'no-cache','organizationid':'be64cce3-44f8-4cd5-9e12-dbfed265165c','secretkey':'0845a386-ab66-4fe8-a1cb-56ef34a3b658'})
    jsonResponse = response.json()
    token = jsonResponse['token']
#now get response
    DATA = '{"query":"'+question+'","pageSize": 1,"pageNumber": 1,"sortOrder": "string","sortBy": "string","languageCode":"en-US","documentType": "Faq","model":"84a0fdf7-6c07-4d17-83da-e4ae17f4ef3e"}'
    response = requests.post(url = 'https://api.genesysappliedresearch.com/v2/knowledge/knowledgebases/7613d1f7-09a7-41f5-a0ba-94f7f6d91d2f/search', data = DATA, headers = {'token':token,'accept':'application/json','Content-Type':'application/json','organizationid':'be64cce3-44f8-4cd5-9e12-dbfed265165c'})
    jsonResponse = response.json()
    print(jsonResponse)
    wut = jsonResponse['results'][0]
    restaurants = wut['faq']['answer']
    print(restaurants)

if __name__ == '__main__':
    app.run(debug=True)
