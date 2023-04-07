import requests
import json
import pyttsx3
print("This is live weather provider for enter city.")
city=input("Please enter the name of city to know weather.\n")
url=f'https://api.weatherapi.com/v1/current.json?key=15c66d8e0fc14d6dbe8131709230604&q={city}'

r=requests.get(url)
# print(r.text)
# print(type(r.text))
wdict=json.loads(r.text)
# print(type(wdict))
tc=wdict ['current'] ['temp_c'] 
wc=wdict ['current']   ['condition'] ['text']
ws=wdict ['current']  ['wind_mph']
h=wdict  ['current'] ['humidity']
s=(f'The weather condition of {city} is as temperature is {tc} celsius, environment is {wc} wind speed is {ws} mph and humidity is {h}.')
speak=pyttsx3.init()
speak.say(s)
speak.runAndWait()