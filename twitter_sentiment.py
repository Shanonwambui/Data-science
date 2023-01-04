import tweepy
from textblob import TextBlob
consumer_key='no8hAWsbDuNFeoUEO7c6GlsUX'
consumer_secret='xlBjW6gLCmrEDwtoMaBwkj7fyieA5fIV51wj77C5J8zWxayFDN'
access_token='1609485346051444736-urmv5kRJx58VQY7fC8qL5eZHoyVyxe'
acces_token_secret='MbsUE4KeOh0gVnmrysyRN2P2gqHLqE8VdWYBVpAp2uwuE'
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,acces_token_secret)
api= tweepy.API(auth)
public_tweets=api.search_tweets('Trump')
for tweet in public_tweets:
    print(tweet.text)
    analysis= TextBlob(tweet.text)
    print(analysis.sentiment)