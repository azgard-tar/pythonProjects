import pyowm

owm = pyowm.OWM('9e90534b10819f0532b3286f4d94f12f', language = "ru")

place = input("В каком городе показать погоду?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

print( "В городе " + place + " сейчас " + w.get_detailed_status() +
"\nТемпература составляет: " + str( w.get_temperature('celsius')["temp"] ) )
