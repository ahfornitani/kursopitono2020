import requests

response = requests.get('http://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
