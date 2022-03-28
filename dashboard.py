import streamlit as st
import pandas as pd
import numpy as np
import requests
import tweepy
import config

# st.title("This is the title")

# st.header("This is a header")

# st.subheader("Subheader")

# st.write("this is regular text")

# """
# # header
# ## subheader
# """

# some_dictionary = {
#     "key": "value",
#     "key2": "value2"
# }


# some_list = [1,2,3]
# st.write(some_dictionary)
# st.write(some_list)

# st.sidebar.title("Options")

# df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))

# st.dataframe(df)

# st.image("https://www.ccn.com/wp-content/uploads/2019/03/Apple-stock-chart.png")

auth = tweepy.OAuth1UserHandler(
#    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

option = st.sidebar.selectbox(
    "Which Dashboard?",
    ('twitter', 'wallstreetbets', 'chart', 'stocktwits', 'chart', 'pattern')
)

st.header(option)

if option == 'twitter':
    for username in config.TWITTER_USERNAMES:
        user = api.get_user(username)
        tweets = api.user_timeline(username)

        st.subheader(username)
        st.image(user.profile_image_url)

        for tweet in tweets:
            if '$' in tweet.text:
                words = tweet.text.split(' ')
                for word in words:
                    if word.startswith('$') and word[1:].isalpha():
                        symbol = word[1:]
                        st.write(tweet.text)
                        st.image(f"somecharthere")

if option == 'chart':
    st.subheader("this is the chart dashboard")

if option == 'wallstreetbets':
    st.subheader("wallstreetbets")

if option == 'pattern':
    st.subheader("pattern")

if option == 'stocktwits':
    symbol = st.sidebar._text_input("Symbol", value='AAPL', max_chars=5)

    r = requests.get()

    data = r.json()

    for message in data['messages']:
        st.write(message['body'])
        st.write(message['created_at'])
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])


