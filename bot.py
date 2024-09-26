#!/usr/bin/env python

import http.client
import json
import sys
from argparse import ArgumentParser


class Bot:
    def send(self, chat_id, message, token):
        data = {'chat_id': chat_id, 'text': message}
        json_data = json.dumps(data)

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        path = '/bot' + token + '/sendMessage'

        connection = http.client.HTTPSConnection('api.telegram.org')
        connection.request('POST', path, json_data, headers)

        response = connection.getresponse()
        return response.read().decode()

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument("-i", "--id", action="store", dest="chat_id", help="Chat ID")

    parser.add_argument("-m", "--message", action="store", dest="message", help="Text message")

    parser.add_argument("-t", "--token", action="store", dest="token", help="Bot's API token")

    args = parser.parse_args()

    if args.chat_id and args.token:
        message = args.message if args.message else sys.stdin.read()
        bot = Bot()
        response = bot.send(chat_id=args.chat_id, message=message, token=args.token)
        print(response)
    else:
        error = {'ok': False, 'error_code': -1, 'description': 'Invalid arguments'}
        print(error)
