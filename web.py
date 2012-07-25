#!/usr/bin/env python

""" The webservice for decisive robot """

import decisiverobot
import os
from flask import Flask
from flask import jsonify
from flask import request
import json

APP = Flask(__name__)

@APP.route('/')
def index():
    """ Serves the landing page """
    return servestatic('index.html')
    
@APP.route('/service/', methods=['GET', 'POST'])
def service():
    """ Json service to answer the user's questions """
    if request.method == 'POST':
        data = json.loads(request.data)
        #todo ensure data['method'] == 'answer'
        question = data['params']['question']
        answer = decisiverobot.answer(question)
        return jsonify(result=answer)
    
    #assume method is GET
    answer = decisiverobot.snarkyanswer(request.args['question'])
    return jsonify(answer=answer)
    
@APP.route('/<requestedfile>.css')
def servestaticcss(requestedfile):
    return servestatic(requestedfile + '.css'), 200, {'Content-Type': 'text/css; charset=utf-8'}
    
@APP.route('/<requestedfile>.svg')
def servestaticsvg(requestedfile):
    return servestatic(requestedfile + '.svg'), 200, {'Content-Type': 'image/svg+xml; charset=utf-8'}
    
@APP.route('/<requestedfile>')
def servestatic(requestedfile):
    """ Serves static web content """
    with file('static/' + requestedfile) as content:
        return content.read()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    PORT = int(os.environ.get('PORT', 5000))
    APP.run(host='0.0.0.0', port=PORT)