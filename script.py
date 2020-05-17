# Simple script that tweets Pi's local IP Address

import tweepy
import socket
import datetime

# Determine current date & time

date = str(datetime.datetime.now())

# Find local IPv4 Address

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localip = s.getsockname()[0]

# Twitter personal details & methods

consumer_key = "Ujc7zvjSbaJyNm8dNDH6IYtrK"
consumer_secret = "UXFDKnQwA0ZvtxcnWtCi6Ccr6KPxN2YrCM52tymSZ3iR8xJUvM"
access_token = "943703667420536832-9uyzndbkf41TFD67ClVBesFOOQcLqcz"
access_token_secret = "pXyOBAb8Pc0FxzW9BGBro2LRXGFPjbDT63KgESefXdaE6"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tweet information

def tweetIP():
    api.update_status(status="({0}) Monkey's IP: {1}".format(date, localip))

if __name__ == '__main__':
    tweetIP()

# Cleaup & final actions. Close socket etc.

s.close()
