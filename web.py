#!/usr/bin/env python

# Copyright 2012 Daniel Kinsman
#
# This file is part of Decisive Robot.
#
# Decisive Robot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Decisive Robot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Decisive Robot.  If not, see <http://www.gnu.org/licenses/>.

""" The webservice for decisive robot """

import decisiverobot
import os
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import json
import urllib

APP = Flask(__name__)

@APP.route('/')
def index():
    """ Serves the landing page """
    if 'question' in request.args:
        question = request.args['question']
        questionurl = "/?question=" + urllib.quote(question)
        answer = decisiverobot.snarkyanswer(question)
    else:
        question = None
        questionurl = None
        answer = None

    return render_template('index.html', question=question,
        questionurl=questionurl, answer=answer)

@APP.route('/service/', methods=['GET', 'POST'])
def service():
    """ Json service to answer the user's questions """
    if request.method == 'POST':
        data = json.loads(request.data)
        #todo ensure data['method'] == 'answer'
        question = data['params']['question']
        answer = decisiverobot.snarkyanswer(question)
        return jsonify(result=answer)

    #assume method is GET
    answer = decisiverobot.snarkyanswer(request.args['question'])
    return jsonify(answer=answer)

@APP.route('/<requestedfile>.css')
def servestaticcss(requestedfile):
    """ Serves static web content with the text/css mime type"""
    return servestatic(requestedfile + '.css'), \
            200, {'Content-Type': 'text/css; charset=utf-8'}

@APP.route('/<requestedfile>.svg')
def servestaticsvg(requestedfile):
    """ Serves static web content with the image/svg+xml mime type"""
    return servestatic(requestedfile + '.svg'), \
            200, {'Content-Type': 'image/svg+xml; charset=utf-8'}

@APP.route('/<requestedfile>')
def servestatic(requestedfile):
    """ Serves static web content """
    # Should really use aws s3 to serve static content, but
    # this is good enough for the low traffic expected now.
    with file('static/' + requestedfile) as content:
        return content.read()

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    PORT = int(os.environ.get('PORT', 5000))
    APP.run(host='0.0.0.0', port=PORT)