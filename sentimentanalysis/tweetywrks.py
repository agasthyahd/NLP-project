#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "313866079-Det7SfwQRji9f8YfurBLWOLp2CcEigPuo7GUVUb6"
access_token_secret = "s6blAATJbgNUmTvIhJl7ON7l9X6vPlzHdN2XJzrh8CkN6"
consumer_key = "vCADb3mQZTDyfyc9y4qPOpui5"
consumer_secret = "uOAQuHCGY9f40D5JX64sZlYX66R2pkO18IK8MfdZRd5umMW1Qr"



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
    stream.filter(languages=['en'],track=['airindiain','airasia','jetairways','Indigo6E','flyspicejet','TK_INDIA','goairlinesindia','British_Airways','emirates','AmericanAir','VirginAir'])
