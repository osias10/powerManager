import os
from flask import Flask, request
import configparser, json

#from flask_cors import CORS
config=configparser.ConfigParser()
if os.path.isfile('./config.ini'):
    config.read('./config.ini',encoding='utf-8')
    password = config['poweroff']['password']
else :
    config['poweroff'] = {}
    config['poweroff']['password'] = 'password'
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET','POST'])
def index():
    return

@app.route('/poweroff', methods=['POST'])
def poweroff():
    if request.method == 'POST':
        params = request.form['password']
        print(params)
        print(password)
        if params == password:
            print("power off")
            os.system("shutdown -s -t 30")
            return str("success power off")
        else:
            print("Failed")
            return "Failed"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=11000)