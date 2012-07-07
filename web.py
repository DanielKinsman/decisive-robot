#!/usr/bin/env python

import decisiverobot
import os
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/json/ask')
def ask():
    print(request.args['q'])
    answer = decisiverobot.answer(request.args['q'])
    return jsonify(answer=answer)
    
@app.route('/<requestedfile>')
def serve(requestedfile):
    return render_template(requestedfile)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)