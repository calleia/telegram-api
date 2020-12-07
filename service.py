#!/usr/bin/env python

import http.client
import json


class Service:
    def send(self, chat_id, message, token):
        data = {'chat_id': chat_id, 'text': message}
        json_data = json.dumps(data)

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

        path = '/bot' + token + '/sendMessage'

        connection = http.client.HTTPSConnection('api.telegram.org')
        connection.request('POST', path, json_data, headers)

        response = connection.getresponse()
        return response.read().decode()
