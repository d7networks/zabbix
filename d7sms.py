#!/usr/bin/python3
# coding=utf-8

# Python2 & 3script for sending sms through D7SMS gateway
# http://d7networks.com

D7TOKEN = "YOUR_D7_TOKEN" # this should be replaced. Can be generated from https://app.d7networks.com/api-tokens

SOURCE_ADDRESS = 'd7-zab' # source address to be used while sending sms
GW_URL = "https://api.d7networks.com/messages/v1/send"

import argparse
import sys
import json
import urllib.request


if __name__ == '__main__':
    content = sys.argv[2].strip('\'')
    to = sys.argv[1].strip('\'').replace(' ','').split(',')  # will be a list of destinations
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + D7TOKEN
    }
    message_globals = {
        "originator": SOURCE_ADDRESS,
    }
    messages = [ 
        {
            "recipients":to,
            "content": content,
            "data_coding": "auto"
        } 
    ]
    json_data = json.dumps({
        "message_globals": message_globals,
        "messages": messages
    })
    
        
    req = urllib.request.Request(GW_URL, data=json_data.encode('utf-8'), headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=10)
    except urllib.error.HTTPError as e:
        print(f"Failed to send sms, reason: {e.reason}, code: {e.code} ")
    else:
        response_data = response.read().decode('utf-8')
        print(response_data)