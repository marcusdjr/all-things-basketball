import snscrape.modules.twitter as sntwitter
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#twitter filter
query = "(#Nbatrades)"
tweets = []
limit = 100

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

# df = pd.read_csv("tweets.csv")

# df.isna().sum()

# text = " ".join(cat.split()[1] for cat in df.category)
# word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
# plt.imshow(word_cloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

