import argparse
import json
import requests
from slackclient import SlackClient
import time

stockurl = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/jsonp?symbol="


# get slack api user token and channel
parser = argparse.ArgumentParser()
parser.add_argument('--slack-token', help="Slack API user token.")
parser.add_argument('--slack-channel', help="Slack channe.")
args = parser.parse_args()
token = args.slack_token
slackchannel = args.slack_channel

# monitor slack api
sc = SlackClient(token)

if sc.rtm_connect():
    sc.rtm_send_message(slackchannel, "STOCKBOT Powering Up!!!")
    while True:

        for slack_message in sc.rtm_read():
            message = slack_message.get("text")
            if 'stock' in str(message):
                symbols = ((str(message).split(':'))[1]).split(';')
                
                for symbol in symbols:
                    r = requests.get(stockurl + symbol)
                    s = json.loads(r.text[18:-1])
                    price = (s['LastPrice'])  
                    sc.rtm_send_message(slackchannel, str(symbol) + ' = ' + str(price))
                
        time.sleep(1)
else:
    print ("Connection Failed, invalid token?")