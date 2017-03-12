import requests
def fetch_weather(city):
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?APPID=aee2077f394cbfc952b3f17e41ffee1e&units=metric&q='+city)
	return r

def pretty_print_weather(city):
	w=fetch_weather(city).json()
	return (w['weather'][0]['description'] + " - " + str(w['main']['temp']) + " degrees C - " + str(w['main']['humidity']) + "% humidity")

print(pretty_print_weather('London'))
