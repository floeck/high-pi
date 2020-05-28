# Simple script that texts your Raspberry Pi's IP to your phone.

import socket
import configparser
from twilio.rest import Client

# Obtain local IP Address

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localip = s.getsockname()[0]

# Load config.ini preferences

user_config = configparser.ConfigParser()
user_config.read('config.ini')

account_sid = user_config["Twilio"]['account_sid']
auth_token = user_config["Twilio"]['auth_token']
receiver = user_config["Twilio"]['to_number']
sender = user_config["Twilio"]['from_number']
message = user_config["Twilio"]['message'] + localip

# Prepare message request

client = Client(account_sid, auth_token)
optional = 0
if user_config["Optional"]['use'] == "true":
    optional = 1
    pi_name = user_config["Optional"]['pi_name']

# Finally, create text function & prepare for script run.

def textIP(optional):
    if optional == 0:
        client.messages.create(to=receiver, from_=sender, body=message)
    elif optional == 1:
        client.messages.create(to=receiver, from_=sender, body="({}) ".format(pi_name) + message)

if __name__ == '__main__':
    textIP(optional)
    s.close()
