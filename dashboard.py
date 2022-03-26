import streamlit as st
import pandas as pd
import numpy as np

st.title("This is the title")

st.header("This is a header")

st.subheader("Subheader")

st.write("this is regular text")

"""
# header
## subheader
"""

some_dictionary = {
    "key": "value",
    "key2": "value2"
}


some_list = [1,2,3]
st.write(some_dictionary)
st.write(some_list)

st.sidebar.write("Write this to the sidebar")

df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))

st.dataframe(df)