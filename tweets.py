import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#Nbatrades)"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.content])
        
df = pd.DataFrame(tweets, columns=['Tweet'])
print(df)

# to save to csv
df.to_csv('tweets.csv')