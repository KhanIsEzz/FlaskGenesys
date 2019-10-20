import requests
with open('/home/alex/Hackathon/HackathonGenesys/ray/restaurants.json', 'r') as file:
    data = file.read()
print(data)
restaurants = 'Manpuku Japanese Eatery:9,No you xd:10'
for restaurant in restaurants.split(','):
        restaurant = restaurant.split(':')
        name = restaurant[0]
	for i in range(0, 3):
		review = data[i+1]
		print(len(review))
		
