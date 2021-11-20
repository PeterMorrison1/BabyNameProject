from matplotlib.pyplot import hist
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from st_aggrid import AgGrid
import plotly.graph_objects as go

@st.cache
def load_baby_names():
    data = pd.read_parquet('./data/fact_names.parquet')
    return data

@st.cache
def load_distinct_names(baby_names):
    return baby_names['name'].drop_duplicates().sort_values()

@st.cache
def load_movie_names():
    data = pd.read_parquet('./data/movies.parquet')
    return data

@st.cache
def load_character_names():
    data = pd.read_parquet('./data/movies_with_characters.parquet')
    return data


# st.set_page_config(layout="wide", page_title="Baby Name Project")
st.title("Baby Name Project")
st.sidebar.title("Baby Name Project")
st.sidebar.caption("by [PeterMorrison1](github.com/PeterMorrison1)")
st.sidebar.write("This is to test the capabilities of Streamlit and explore baby name data.")

baby_names = load_baby_names()
distinct_names = load_distinct_names(baby_names)
movies = load_movie_names()
characters = load_character_names()

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

st.header("Name Popularity by Year")
name_select = st.selectbox("Pick a name to chart popularity", distinct_names)
name_data = baby_names[baby_names['name'] == name_select]
fig = px.histogram(name_data, x=name_data['year'], y=name_data['count'])
st.plotly_chart(fig, use_container_width=True)

st.write("Name popularity by Year and State")
fig = px.line(name_data, x=name_data['year'], y=name_data['count'], color=name_data['prov_state_id'])
st.plotly_chart(fig, use_container_width=True)

st.header("Actor/Movie comparison")

# select and group by name/year
selected_movie_filter = movies[movies['actors'].str.startswith(name_select)]
grouped_movie_names = selected_movie_filter.groupby(['year']).size().reset_index(name='count')



selected_character_filter = characters[characters['characters'].str.startswith(name_select)]
grouped_character_names = selected_character_filter.groupby(['year']).size().reset_index(name='count')

AgGrid(selected_movie_filter)
AgGrid(selected_character_filter)

st.write('## Births and Theatrical Releases by year and name (birth, actor, and character name)') 
fig = go.Figure()
fig.add_trace(go.Histogram(x=name_data['year'], y=name_data['count'], name='Births'))
fig.add_trace(go.Histogram(x=grouped_movie_names['year'], y=grouped_movie_names['count'], name=f'Actors starting with {name_select}'))
fig.add_trace(go.Histogram(x=grouped_character_names['year'], y=grouped_character_names['count'], name=f'Characters starting with {name_select}'))
fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.75)
st.plotly_chart(fig, use_container_width=True)

