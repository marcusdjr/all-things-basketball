import snscrape.modules.twitter as sntwitter
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

#twitter filter
query = "(#Nbatrades)"
tweets = []
limit = 5000

#for loop for printing content
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.content])
        
#printing to csv file
df = pd.DataFrame(tweets, columns=['Tweet'])
print(df)

# save to csv file
df.to_csv('tweets.csv')

# Read text
text = open('tweets.csv', mode='r', encoding='utf-8').read()

#STOPWORDS
stopwords = ('stopwords.txt')

wc = WordCloud(
    background_color='white',
    stopwords=stopwords,
    height = 600,
    width= 400
)

wc.generate(text)

#storing word cloud to file
wc.to_file('wordcloud_output.png')