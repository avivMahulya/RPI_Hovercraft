from flask import Flask
from flask import request
import logging
import json
import TargetMovement as mv
import threading
import time
#disable flask logging,show only errors
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
timer = 0;
app = Flask(__name__)
WD_timeout = 0.5 #0.5 seconds
is_message_received = False
firstCommandReceived = False

def checkTimeout():
    global is_message_received
    global motor_control
    while not firstCommandReceived:
        time.sleep(WD_timeout)
    while True:
        if not is_message_received:
            motor_control.stop()
        else:
            is_message_received = False
        time.sleep(WD_timeout)
WD_thread = threading.Thread(target=checkTimeout)
WD_thread.start()

motor_control = mv.MotorControl()

motor_control.initialize_motors()
motor_control.arm()
@app.route('/registrazione', methods=['GET', 'POST'])

@app.route("/",methods=['GET', 'POST'])
def getCommands():
    global firstCommandReceived
    global is_message_received
    if not firstCommandReceived:
        firstCommandReceived = True;
    is_message_received = True
    isCommandExists = False
    print(json.loads(request.data))
    if json.loads(request.data)['forward'] > 0:
        isCommandExists = True
        motor_control.forward()
    if json.loads(request.data)['back'] > 0:
        isCommandExists = True
        motor_control.backward()
    if json.loads(request.data)['left'] > 0:
        isCommandExists = True
        motor_control.left()
    if json.loads(request.data)['right'] > 0:
        isCommandExists = True
        motor_control.right()
    if json.loads(request.data)['stop'] == True:
        motor_control.stop()
    return "a"

if __name__ == '__main__':
   app.run(host='0.0.0.0')