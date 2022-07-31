import os
import tweepy as tw
import pandas as pd
from geopy import geocoders
from geopy.geocoders import Nominatim


class GetTweetLocatin:
    def getLocations(self, tweet):
        search_words = "#" + tweet
        date_since = "2018-11-16"
        consumer_key = 'kU5EnStGNVvMU2J9Ni0dsiITj'
        consumer_secret = '26HZTTQjiGSwBIhyiVt7LzlTXzD1d5WHgetr586FPS4rhbqVaj'
        access_token = '1089021744336244737-XdMHpwoCZKZuPHqPwqjoG9v8vDEdjI'
        access_token_secret = 'kq2cS2Q6IrwmadqbMKFBh2cfqJKTXhNvKW0Cki86W9oc6'
        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        # Collect tweets
        tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(50)
        print("=====>", tweets.__dict__)

        users_locs = [[tweet.id, tweet.user.name, tweet.created_at, tweet.user.screen_name, tweet.text,
                       tweet.user.location, tweet.coordinates] for tweet in tweets]
        # print(users_locs)
        dataframe = pd.DataFrame(data=users_locs,
                                  columns=['Tweet ID', 'User Name', 'Created at', 'User Screen Name', "Tweets",
                                           'Tweet Location', 'User Location'])
        #gn = geocoders.GeoNames()
        #print(gn.geocode("Cleveland, OH 44106"))
        return users_locs, dataframe

        # return users_locs

    def getLatitudeLongitude(self,cityname):
        geolocator = Nominatim(user_agent="datapointprojects13@gmail.com")
        location = geolocator.geocode(cityname)
        try:
            return location.latitude, location.longitude,location.address
        except Exception as ex:
            return 0,0,None
