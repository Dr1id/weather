import eel
from pyowm import OWM

owm = OWM('4ab8702aaf30304e2f6927c032d2cb36')

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    t = w.temperature('celsius')
    t1 = t['temp']
    return "В городе " + place + " сейчас " + str(t1) + " градусов."

eel.init("web")
eel.start("main.html", size=(600, 450))