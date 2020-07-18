import requests
import json

defaultServerIP = '192.168.1.27'

def build_url(page):
    return "http://" + defaultServerIP +"/" + page

def initConnection():
       r = requests.get('http://192.168.1.27:5000/registrazione/')
#receives dictionary of commands and send JSON object
def sendCommands(commandsDict):
    commandsJson = json.dumps(commandsDict)
   # session = requests.Session(default_host="http://192.168.1.27")
    r = requests.post('http://192.168.1.27:5000/',data = commandsJson)
    if ((r.status_code >= 200) and (r.status_code < 208)):
        status = True
    else:
        status = False
        
    return status


    