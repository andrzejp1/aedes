import datetime
import requests
import ConfigParser
class Sensor:
    def __init__(self, prefix, json):
        self.temperature = 70;
        self.humidity = 50;
        self.battery = 80;
        if prefix + 'temperature' in json:
            self.temperature = float(json[prefix + 'temperature'])
        if prefix + 'humidity' in json:
            self.humidity = float(json[prefix + 'humidity'])
        if prefix + 'battery' in json:
            self.battery = int(json[prefix + 'battery'])

class Switch:
    def __init__(self, name, json):
        self.state = False
        if name in json:
            if json[name] == 'on':
                self.state = True

class LabState:
    def __init__(self,json):
        self.Front = Sensor('front-', json)
        self.Back = Sensor('back-', json)
        self.Heat = Switch('heat-state', json)
        self.Fogger = Switch('fogger-state', json)
        self.Vent = Switch('vent-state', json)

config = ConfigParser.ConfigParser()
config.read('/media/pi/data/aedes.cfg')

def CurrentStateNoCache():
    url=config.get('main','url')
    auth_token=config.get('main','token')
    headers = {'Authorization': 'Bearer '+ auth_token}
    r = requests.get(url, headers=headers)
    # print r.json()
    return LabState(r.json())

# Don't ping webservice more often than every 60 seconds2
cachedState = CurrentStateNoCache()
cachedTime = datetime.datetime.now()
def CurrentStatus():
    global cachedState
    global cachedTime
    if (datetime.datetime.now()-cachedTime).total_seconds() > 60:
        cachedState = CurrentStateNoCache()
        cachedTime = datetime.datetime.now()
    return cachedState










