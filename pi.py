'''
A basic Twitter Bot to tweet Pi to anyone who tweets to it.
@author @TheDestruc7i0n
'''
try: import simplejson as json #Get a faster version of json, if this fails just import normal json
except ImportError: import json

import tweepy, time #For timing
from tweepy import Stream, StreamListener #To get a live stream of tweets that you can reply to
from decimal import Decimal #To put pi into a decimal

METHOD = "CONSOLE"
TWITTER_CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
TWITTER_CONSUMER_SECRET = "TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_KEY = "TWITTER_ACCESS_KEY"
TWITTER_ACCESS_SECRET = "TWITTER_ACCESS_SECRET"
SELF_ID = "1234567890" #Find this when making the app on Twitter

TWITTER_HANDLE = "@tweetedpi" #You may change based on your handle

#Now to authenticate
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

pi = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196")
#First 200 digits of Pi after the decimal

class customStreamListener(StreamListener):
	'''
	The main code
	'''
	def on_data(self, data):
		print "%s: Started at %s" % (METHOD, time.ctime()) #Debug
		jdata = json.loads(data.strip())
		print METHOD+": Tweet from @"+jdata.get("user",{}).get("screen_name")+": "+jdata.get("text")
		retweeted = jdata.get("retweeted")
		from_self = jdata.get("user",{}).get("id_str","") == SELF_ID #Make sure not from self!
		
		if retweeted is not None and not retweeted and not from_self:
			'''
			Now for the real part, the part before is just to make sure that the bot should answer
			'''
			reply_to = jdata.get('user',{}).get('screen_name') #Get screen name for whom to reply to
			reply_to_id = jdata.get("user",{}).get("id_str","") #Get id of user to reply to
			begin = 0
			end = 138-len(jdata.get('user',{}).get('screen_name')) #Get as much pi as it can into a tweet
			tweet = "@"+reply_to+" "+str(pi)[begin:end] #Get pi and put it into a tweet
			api.update_status(tweet, in_reply_to_status_id = reply_to_id) #This replies
			print METHOD+": Replied to @"+reply_to+" with '"+str(pi)[begin:end]+"' ("+str(len(str(pi)[begin:end]))+" digits)" #Print how many digits of pi printed and the tweet
			print "%s: Ended at %s" % (METHOD, time.ctime()) #Debug

	def on_error(self, error):
		print METHOD+": "+str(error) #Print error
		time.sleep(5) #Wait 5 seconds and try again
		return True
		

def main():
	'''
	Just to activate Listener
	'''
	l = customStreamListener()
	stream = Stream(api.auth, l)
	while 1:
		stream.filter(track=[TWITTER_HANDLE])

if __name__ == "__main__": main()
