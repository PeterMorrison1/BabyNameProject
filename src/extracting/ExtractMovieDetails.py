import numpy as np
import pandas as pd
from ast import literal_eval

temp_folder = './temp/'

movies = pd.read_csv(temp_folder + 'IMDb_movies.csv')
# names = pd.read_csv(temp_folder + 'IMDb_names.csv')
title_principals = pd.read_csv(temp_folder + 'IMDb_title_principals.csv')

# print(movies)
# print(names)
# print(title_principals)

# df = title_principals.join([movies.reset_index(drop=True), names.reset_index(drop=True)])
# df = title_principals.merge(movies)
# print(title_principals.groupby(['imdb_title_id']))
# title_principals['imdb_title_id'] = title_principals['imdb_title_id'].apply(str)[0]
# # title_principals['characters'] = title_principals['characters'].apply(str)[0]
# title_principals = title_principals.dropna()

# print(title_principals)
# title_principals = title_principals.query("cateogry = 'actress' or category = 'actor'")
# # title_principals = title_principals.drop(title_principals[title_principals['category'] != 'actress'].index)
# # title_principals = title_principals.drop(title_principals[title_principals['category'] != 'actor'].index)
# title_principals = title_principals.drop(['job', 'category', 'ordering'], axis=1)
# title_principals = title_principals.drop_duplicates()
# print(title_principals)


df = movies.copy()


df = df[['year', 'actors', 'title', 'imdb_title_id', 'avg_vote']]
df.set_index(['year', 'title', 'imdb_title_id', 'avg_vote'])
df['actors'] = df['actors'].apply(lambda x: str(x).split(','))

final = df.explode('actors').reset_index()
final['year'] = final['year'].astype(str).astype(int)

# final.to_parquet('./data/movies.parquet')

# Merge to get the characters #! Need to match actor/actress to character 
# title_principals['characters'].replace('', np.nan, inplace=True)
# title_principals.dropna(subset=['characters'], inplace=True)
# merged = pd.merge(final, title_principals[['imdb_title_id', 'category', 'characters']], on='imdb_title_id', how='left')
# print(merged)

# final_merged = merged.explode('characters').reset_index()

# print(final_merged)

df = title_principals.copy()


df = df[['characters', 'imdb_title_id']]
df.set_index(['imdb_title_id'])
# df['characters'] = df['characters'].apply(lambda x: str(x).split(','))
df.dropna(subset=['characters'], inplace=True)
df['characters'] = df['characters'].apply(literal_eval)

final = df.explode('characters').reset_index()
# print(final)


merged = pd.merge(final, movies[['imdb_title_id', 'year', 'title']], on='imdb_title_id', how='left')
print("Merged")
print(merged)

# final['year'] = final['year'].astype(str).astype(int)
merged.to_parquet('./data/movies_with_characters.parquet', index=True)