import GetOldTweets3 as got
import pandas as pd

keyword = "#amazonlocker"
oldest_date = "2017-01-01"    
newest_date = "2020-30-01"
number_tweets = 100         #per location


#get old tweets
tweet_criteria = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                            .setSince(oldest_date)\
                                            .setUntil(newest_date)\
                                            .setMaxTweets(number_tweets)
#extract twitter information
tweet_df = pd.DataFrame({'got_criteria':got.manager.TweetManager.getTweets(tweet_criteria)})
tweet_df["tweet_text"] = tweet_df["got_criteria"].apply(lambda x: x.text)
tweet_df["date"] = tweet_df["got_criteria"].apply(lambda x: x.date)
tweet_df["hashtags"] = tweet_df["got_criteria"].apply(lambda x: x.hashtags)
tweet_df["link"] = tweet_df["got_criteria"].apply(lambda x: x.permalink)
tweet_df = tweet_df.drop("got_criteria", 1)
tweet_df.head()
    


#export
tweet_df.to_csv("Twitter2_data.csv")
