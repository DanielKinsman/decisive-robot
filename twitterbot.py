#!/usr/bin/env python

""" Twitter bot for automatically replying to questions
    asked to @decisiverobot on twitter """

# Stolen shamelessly from https://github.com/vivekhaldar/the_shrinkbot/blob/master/the_shrink.py
# See http://blog.vivekhaldar.com/post/2830035130/how-to-write-a-twitter-bot-in-python

from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

import os
import time
import sys
import re

import decisiverobot

CONSUMER_KEY='replacethis'
CONSUMER_SECRET='replacethis'
ACCESS_TOKEN='replacethis'
ACCESS_TOKEN_SECRET='replacethis'
TWITTER_USER = "@replacethis"
REG_REMOVE_USER = re.compile(r'^' + TWITTER_USER, re.IGNORECASE)
SLEEP_INTERVAL = 30
LAST_ID_FILE = 'twitterbot.lastid'

if __name__ == '__main__':
    # We use two twitter clients, one to search, another to update. Just
    # easier that way...
    twitter = Twitter(domain='search.twitter.com')
    twitter.uriparts=()

    last_id_replied = ''
    
    try:
        with file(LAST_ID_FILE, 'r') as content:
            last_id_replied = content.read()
    except IOError as ex:
        print(LAST_ID_FILE + " not found")

    poster = Twitter(
        auth=OAuth(
            ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET),
        secure=True,
        api_version='1',
        domain='api.twitter.com')

    while True:
        results = twitter.search(q=TWITTER_USER, since_id=last_id_replied)['results']

        for result in results:
            # Remove our twitter name from the question.
            question = REG_REMOVE_USER.sub('', result['text'])
            asker = result['from_user']
            question_id = str(result['id'])
            print(" <<< " + asker + ": " + question)

            bot_response = decisiverobot.snarkyanswer(question)
            
            msg = '@{0} {1}'.format(asker, bot_response)
            print('====> Resp =' + msg)
            last_id_replied = question_id
            poster.statuses.update(status=msg)
            
            print('Last id replied to = ', last_id_replied)
            
            try:
                with file(LAST_ID_FILE, 'w') as writer:
                    writer.write(last_id_replied)
            except IOError as ex:
                print(ex)

        time.sleep(SLEEP_INTERVAL)