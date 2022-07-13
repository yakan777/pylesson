import requests
import json
from pprint import pprint
'''
s='ab' 'bc'
print(s)
'''
url = ('https://api.openweathermap.org/data/2.5/weather'
'?zip={zip}&appid={key}&lang=ja&units=metric')
url=url.format(zip='160-0006,JP',key='474278bda6547b3150b6d7bfb5d69516')

jsondata=requests.get(url).json()
#pprint(jsondata)

print('都市名:',jsondata['name'])
print('気温:',jsondata['main']['temp'])
print('天気:',jsondata['weather'][0]['main'])
print('天気詳細:',jsondata['weather'][0]['description'])
