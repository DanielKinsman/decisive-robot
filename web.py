#!/usr/bin/env python

import decisiverobot
import os
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return serve('index.html')
    
@app.route('/service/', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        data = json.loads(request.data)
        #todo ensure data['method'] == 'answer'
        question = data['params']['question']
        answer = decisiverobot.answer(question)
        return jsonify(result=answer)
    
    answer = decisiverobot.answer(request.args['q'])
    return jsonify(answer=answer)
    
@app.route('/<requestedfile>')
def serve(requestedfile):
    with file('static/' + requestedfile) as f:
        return f.read()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)