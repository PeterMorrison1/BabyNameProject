from matplotlib.pyplot import hist
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from st_aggrid import AgGrid

@st.cache
def load_baby_names():
    data = pd.read_parquet('./data/fact_names.parquet')
    return data

@st.cache
def load_distinct_names(baby_names):
    return baby_names['name'].drop_duplicates().sort_values()

# st.set_page_config(layout="wide", page_title="Baby Name Project")
st.title("Baby Name Project")
st.sidebar.title("Baby Name Project")
st.sidebar.caption("by [PeterMorrison1](github.com/PeterMorrison1)")
st.sidebar.write("This is to test the capabilities of Streamlit and explore baby name data.")

baby_names = load_baby_names()
distinct_names = load_distinct_names(baby_names)

names_after_2019 = baby_names['year'] > 2019

df = baby_names[names_after_2019]

year_min = st.slider("Pick start date", 1910, 2020, 2020)
year_max = st.slider("Pick end date", 1910, 2020, 2020)
year_range_filter = (baby_names['year'] >= year_min) & (baby_names['year'] <= year_max)
filtered_df = baby_names[year_range_filter]


show_states = st.checkbox("Do you want to see individual states?")



if show_states:
    filter_by_state = st.checkbox("Do you want to filter by state?")
    if filter_by_state:
        state_filter = st.multiselect("Pick state to filter by", baby_names['prov_state_id'].drop_duplicates())
        filtered_df = filtered_df[filtered_df['prov_state_id'].isin(state_filter)]
    filtered_df.sort_values(by=['prov_state_id', 'year', 'sex', 'count', 'name'], inplace=True, ascending=False)

else:
    filtered_df = filtered_df.groupby(['name', 'sex', 'year'], as_index=False).agg({'count':'sum'})
    filtered_df.sort_values(by=['year', 'sex', 'count', 'name'], inplace=True, ascending=False)
AgGrid(filtered_df)


name_select = st.selectbox("Pick a name to chart popularity", distinct_names)
name_data = baby_names[baby_names['name'] == name_select]
fig = px.histogram(name_data, x=name_data['year'], y=name_data['count'])
st.plotly_chart(fig, use_container_width=True)