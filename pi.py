'''
Placeholder for now
'''
import tweepy
from tweepy import Stream, StreamListener #To get a live Stream of tweets
from decimal import *

TWITTER_CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
TWITTER_CONSUMER_SECRET = "TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_KEY = "TWITTER_ACCESS_KEY"
TWITTER_ACCESS_SECRET = "TWITTER_ACCESS_SECRET"

TWITTER_HANDLE = "@tweetedpi" #You may change based on the handle

#Now to authenticate
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

pi = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196")
#First 200 digits of Pi after the decimal

class customStreamListener():
  '''
  The main code
  '''

def main():
  '''
  Just to activate Listener
  '''
  c = customStreamListener()

if __name__ == "__main__": main()
