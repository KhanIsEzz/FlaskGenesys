#this curls the shit
import subprocess

token = subprocess.check_output(["curl",'-X','POST','https://api.genesysappliedresearch.com/v2/knowledge/generatetoken'])#,'-H',"'Accept: */*'",'-H',"'cache-control: no-cache'",'-H',"'organizationid: be64cce3-44f8-4cd5-9e12-dbfed265165c'",'-H',"'secretkey: 0845a386-ab66-4fe8-a1cb-56ef34a3b658'"])
#answer = subprocess.check_output(["curl","-d",'{"query": "What is the best restaurant in Toronto?","pageSize": 5,"pageNumber": 1,"sortOrder": "string","sortBy": "string","languageCode":"en-US","documentType": "Faq"}','-X','POST','https://api.genesysappliedresearch.com/v2/knowledge/knowledgebases/7613d1f7-09a7-41f5-a0ba-94f7f6d91d2f/search','-H',"token:",token])

