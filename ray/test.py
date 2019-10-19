import requests
answer = 'yummy thai:5,No you xd:10'
for i in answer.split(','):
	for x in i.split(':'):
		print(x)
