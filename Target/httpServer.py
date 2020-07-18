from flask import Flask
from flask import request
import logging

#disable flask logging,shaw only errors
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/registrazione', methods=['GET', 'POST'])

@app.route("/",methods=['GET', 'POST'])
def getCommands():
    print(request.data)
    
   return "a"

if __name__ == '__main__':
   app.run(host='0.0.0.0')