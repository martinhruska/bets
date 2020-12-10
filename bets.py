#! /usr/bin/python3

import sys
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Ridge

# load the data.
#df = pd.read_csv('hockey_games.csv', skiprows=1, names=['date', 'visitor', 'visitor_goals', 'home', 'home_goals', 'unknown', 'att', 'log', 'notes'])
df = pd.read_csv(sys.stdin, skiprows=1, names=['div','date','time', 'home', 'visitor', 'home_goals', 'visitor_goals'])

# make the date column into a date format.
# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

df['goal_difference'] = df['home_goals'] - df['visitor_goals']

df['home_win'] = np.where(df['goal_difference'] > 0, 1, 0)
df['home_loss'] = np.where(df['goal_difference'] < 0, 1, 0)

df_visitor = pd.get_dummies(df['visitor'], dtype=np.int64)
df_home = pd.get_dummies(df['home'], dtype=np.int64)

df_model = df_home.sub(df_visitor) 
df_model['goal_difference'] = df['goal_difference']

df_train = df_model # not required but I like to rename my dataframe with the name train.

lr = Ridge(alpha=0.001) 
X = df_train.drop(['goal_difference'], axis=1)
y = df_train['goal_difference']

lr.fit(X, y)

df_ratings = pd.DataFrame(data={'team': X.columns, 'rating': lr.coef_})
print(df_ratings)

srt=sorted(list(zip(X.columns,lr.coef_)), key=lambda x: x[1])
print(srt)
