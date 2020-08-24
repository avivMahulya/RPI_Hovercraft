from flask import Flask
from flask import request
import logging
import json
import TargetMovement as mv
#disable flask logging,shaw only errors
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

motor_control = mv.MotorControl()

motor_control.initialize_motors()
motor_control.arm()
@app.route('/registrazione', methods=['GET', 'POST'])

@app.route("/",methods=['GET', 'POST'])
def getCommands():
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