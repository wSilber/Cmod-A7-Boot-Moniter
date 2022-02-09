from flask import Flask, render_template, request, redirect, jsonify
import json
from richarduino import Richarduino

# Create flask app
app = Flask(__name__)

# Richarduino serial variables
port = 10
baudrate = 115200
timeout = 2

# Give client html page on root request
@app.route('/')
def hello():
    return render_template('index.html')

# Poke Richarduino on poke request
@app.route('/poke', methods=['GET', 'POST'])
def poke():
    address = request.get_json()['address']
    data = request.get_json()['data']
    richarduino = Richarduino('com' + str(port), baudrate, timeout)
    richarduino.poke(address, data)
    return json.dumps({'success': 'true'})

# Peek Richarduino on peek request
@app.route('/peek', methods=['GET', 'POST'])
def peek():
    address = request.get_json()['address']
    richarduino = Richarduino('com' + str(port), baudrate, timeout)
    resp = str(richarduino.peek(address))
    newData = {'data': resp}
    return jsonify(newData)

# Get version from Richarduino on version request
@app.route('/version')
def version():
    richarduino = Richarduino('com' + str(port), baudrate, timeout)
    version = {"version" :richarduino.getVersion()}
    return json.dumps(version)

# Program Richarduino on program request
@app.route('/program', methods=['GET', 'POST'])
def program():
    if request.method == 'POST':
        f = request.files['file']
        richarduino = Richarduino('com' + str(port), baudrate, timeout)
        richarduino.program(f)
    return redirect('/')