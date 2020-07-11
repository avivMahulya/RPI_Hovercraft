from Host import Controller
from btcom import *  # TigerJython
from btpycom import *  # Standard-Python (PC, Raspi, ...)

def setupConnection(serverName):
    serviceName = serverName
    print("Performing search for service name:", serviceName)
    client = BTClient(stateChanged=onStateChanged)
    serverInfo = client.findService(serviceName, 20)
    if serverInfo is None:
        print("Service search failed")
        return None
    else:
        print("Got server info", serverInfo)
        if client.connect(serverInfo, 20):
            return client
        else:
            print("Unable to connect to server")
            return None

client = setupConnection("BTHover")

CommandsDict = {
    "h": lambda x: toggleHover(1),
    "w": lambda x: moveForward(15),
    "s": lambda x: moveBackward(15),
    "a": lambda x: turn(-15),
    "d": lambda x: turn(15),
}[value](x)


if client is not  None:
    key = input()
    while key != 27: #27 is ESC ascii code
        key = input()
        if key in CommandsDict:
            client.sendMessage(CommandsDict[key])

    client.disconnect()
else:
    print("Unable to connect")

