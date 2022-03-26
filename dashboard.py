import streamlit as st
import pandas as pd
import numpy as np
import requests

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

option = st.sidebar.selectbox(
    "Which Dashboard?",
    ('twitter', 'wallstreetbets', 'chart', 'stocktwits', 'chart', 'pattern')
)

st.header(option)

if option == 'twitter':
    st.subheader("twitter dashboard logic")

if option == 'chart':
    st.subheader("this is the chart dashboard")

if option == 'stocktwits':
    # st.subheader('stocktwits')

    r = requests.get()

    data = r.json()

    for message in data['messages']:
        st.write(message['body'])
        st.write(message['created_at'])
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])


