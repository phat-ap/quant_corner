# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:26:10 2023

@author: phata
"""

# !pip install streamlit

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Set the title and description of the app
st.title("Data extract and plot")
st.write("Extract")

@st.cache_data
def get_cpi_series():
    data = requests.get(
        "https://dataapi.moc.go.th/cpig-indexes?region_id=5&index_id=" +
        "0000000000000000" +
        "&from_year=" + str(2001) +
        "&to_year=" + str(2100)
        )
    df = pd.DataFrame(data.json())
    df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str)
    df.index = pd.to_datetime(df['date'])
    return df['price_index'].rename("CPI")    

df = get_cpi_series()
st.write(df)

st.write("Calculate")
st.write("Latest MoM:", f"{round(df.iloc[-1]/df.iloc[-2]*100-100, 3)}%")
st.write("Latest YoY:", f"{round(df.iloc[-1]/df.iloc[-13]*100-100, 3)}%")

st.write("Plot")
fig, ax = plt.subplots()

df_yoy = (df/df.shift(12)*100-100).dropna()

ax.plot(df_yoy.index, df_yoy)
ax.set_xlabel("Time")
ax.set_ylabel("%YoY")
ax.set_title("CPI")

# Display the chart in the Streamlit app
st.pyplot(fig)