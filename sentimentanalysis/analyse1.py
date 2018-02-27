from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
from nltk import *
tweets_data_path = 'jsncmnts.txt'
j=0
tweets_data = {}
tweet_sent=[]
fo = open("tweetsentn.txt", "rw+")
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweets_data= json.loads(line)
        tweet_sent.append(str(tweets_data['text']))
        fo.write((tweets_data['text'])
                 
        


                 
    except:
         continue
fo.close()
sid = SentimentIntensityAnalyzer()
for sentence in tweet_sent:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
             print('{0}: {1},'.format(k, ss[k]))
             print()

