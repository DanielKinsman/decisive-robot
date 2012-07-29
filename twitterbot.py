#!/usr/bin/env python

""" Twitter bot for automatically replying to questions
    asked to @decisiverobot on twitter """

# Stolen shamelessly from:
# github.com/vivekhaldar/the_shrinkbot/blob/master/the_shrink.py
# blog.vivekhaldar.com/post/2830035130/how-to-write-a-twitter-bot-in-python

from twitter.api import Twitter
from twitter.oauth import OAuth

import time
import re
import traceback

import decisiverobot

# Get your keys from https://dev.twitter.com/apps/new
CONSUMER_KEY = 'replacethis'
CONSUMER_SECRET = 'replacethis'
ACCESS_TOKEN = 'replacethis'
ACCESS_TOKEN_SECRET = 'replacethis'
TWITTER_USER = "@replacethis"

REG_USER_BEGINNING = re.compile(r'^\.?' + TWITTER_USER, re.IGNORECASE)
SLEEP_INTERVAL = 30
LAST_ID_FILE = 'twitterbot.lastid'

def run():
    """ Runs the bot it a loop, checking for questions and replying """

    # We use two twitter clients, one to search, another to update. Just
    # easier that way...
    twitter = Twitter(domain='search.twitter.com')
    twitter.uriparts = ()

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
        results = twitter.search(
            q=TWITTER_USER,
            since_id=last_id_replied)['results']

        for result in results:
            last_id_replied = str(result['id'])
            question = result['text']

            # Only answer tweets with username at the beginning
            if REG_USER_BEGINNING.match(question) is None:
                continue

            # Remove our twitter name from the question.
            question = REG_USER_BEGINNING.sub('', question)
            asker = result['from_user']
            print(" <<< " + asker + ": " + question)

            bot_response = decisiverobot.snarkyanswer(question)
            
            msg = '@{0} {1}'.format(asker, bot_response)
            print('====> Resp =' + msg)
            poster.statuses.update(status=msg, in_reply_to_status_id=last_id_replied)
            
            try:
                with file(LAST_ID_FILE, 'w') as writer:
                    writer.write(last_id_replied)
            except IOError as ex:
                print(ex)

        time.sleep(SLEEP_INTERVAL)

if __name__ == '__main__':
    while True:
        try:
            run()
        except:
            print(traceback.format_exc())

        time.sleep(SLEEP_INTERVAL)