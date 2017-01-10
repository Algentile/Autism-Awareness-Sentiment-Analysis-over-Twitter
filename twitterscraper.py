from tweepy import StreamListener
from tweepy import OAuthHandler 
from tweepy import Stream
import json

access_token = "792972343316480000-2Ts9qvLmDXnOpzeTtqSsqXP3qnV9z8l"
access_token_secret = "CMSF7hvj8DXt3YIHrCLSzoyiRGG9kqA5uUKWBuAk0iKsO"
consumer_key = "wOzaHKiiR4ou8cWwiy0Wd7iTn"
consumer_secret = "oqTW2vhWFGvm90VJx0eUBvDIi03glBeqFBHyBs0PDmbQzgve5P"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Autism'])
