import GetOldTweets3 as got
import pandas as pd

#set search variables
keyword = "#amazonlocker"
oldest_date = "2017-01-01"    
newest_date = "2020-01-01"
locations = ["Austin", "New York", "Los Angeles", "San Francisco", "Chicago","USA","japan","Seattle","London"]

number_tweets = 1000

#get old tweets
tweetCriteria_list = []
for location in locations:
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                           .setSince(oldest_date)\
                                           .setUntil(newest_date)\
                                           .setNear(location)\
                                           .setMaxTweets(number_tweets)
                                           
    tweetCriteria_list.append(tweetCriteria)

#create twitter info for each city
tweet_dict = {}
for criteria, location in zip(tweetCriteria_list, locations):
    tweets = got.manager.TweetManager.getTweets(criteria)
    tweet_dict[location] = tweets 

#create df
tweet_df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in tweet_dict.items() ]))
tweet_df['tweet_count'] = tweet_df.index
tweet_df = pd.melt(tweet_df, id_vars=["tweet_count"], var_name='City', value_name='got_criteria')
tweet_df = tweet_df.dropna()

#extract twitter information
tweet_df["tweet_text"] = tweet_df["got_criteria"].apply(lambda x: x.text)
tweet_df["date"] = tweet_df["got_criteria"].apply(lambda x: x.date)
tweet_df["hashtags"] = tweet_df["got_criteria"].apply(lambda x: x.hashtags)
tweet_df["link"] = tweet_df["got_criteria"].apply(lambda x: x.permalink)
tweet_df = tweet_df.drop("got_criteria", 1)
tweet_df.head()

#export
tweet_df.to_csv("TwitterAmazon3_data.csv")
