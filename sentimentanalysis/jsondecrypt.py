from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

tweets_data_path = 'jsncmnts4.txt'
j=0
tweets_data = {}
tweet_sent=[]
fo = open("tweetsentn4.txt", "rw+")
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweets_data= json.loads(line)
        tweet_sent.append(str(tweets_data['text']))
        fo.seek(0,2)
        fo.write(tweets_data['text'])
        fo.write("\n")
        
        
    
    except:
        continue

fo.close()
sid = SentimentIntensityAnalyzer()
for sentence in tweet_sent:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
             print('{0}: {1}, '.format(k, ss[k]))
             
