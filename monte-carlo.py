#! /usr/bin/python3

import sys
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Ridge
import scipy.stats as st
from scipy.stats._continuous_distns import _distn_names
import scipy

def get_best_distribution(data):
    # dist_names = ["norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme", "gamma", "beta", "rayleigh"]
    dist_names = ["norm",  "pareto"]
    dist_results = []
    params = {}
    for dist_name in dist_names: #_distn_names:
        #if dist_name in {"geninvgauss", "levy_stable"}:
        #  continue
        dist = getattr(st, dist_name)
        param = dist.fit(data)

        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = st.kstest(data, dist_name, args=param)
        print("p value for "+dist_name+" = "+str(p))
        dist_results.append((dist_name, p))

    # select the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value

    print("Best fitting distribution: "+str(best_dist))
    print("Best p value: "+ str(best_p))
    print("Parameters for the best fit: "+ str(params[best_dist]))

    return best_dist, best_p, params[best_dist]

def simulate_game(home_dist_name, home_param, visitor_dist_name, visitor_param):
    home_dist = getattr(scipy.stats, home_dist_name)
    visitor_dist = getattr(scipy.stats, visitor_dist_name)
    
    games = 1000
    results = [0,0,0]
    for i in range(0,games):
      home_score = round(float(home_dist.rvs(*home_param[:-2], loc=home_param[-2], scale=home_param[-1], size=1)))
      away_score = round(float(visitor_dist.rvs(*visitor_param[:-2], loc=visitor_param[-2], scale=visitor_param[-1], size=1)))
      if home_score > away_score:
        results[0] = results[0] + 1
      elif home_score == away_score:
        results[1] = results[1] + 1
      elif home_score < away_score:
        results[2] = results[2] + 1
    percents = [results[0]/games, results[1]/games, results[2]/games, (results[0]+results[1])/games, (results[1]+results[2])/games]
    odds = []
    for i in percents:
      odds.append(1/i)
    print(results)
    print(percents)
    print(odds)
    return (results,percents,odds)
 
def simulate_match(map_to_dist, team1_name, team2_name):
  print(team1_name + " vs. " +team2_name)
  team1 = team_to_dist[team1_name]
  team2 = team_to_dist[team2_name]
  return simulate_game(team1[0],team1[1],team2[0],team2[1])

def simulate_all(team_to_dist):
  sim_teams = set()
  for team1 in team_to_dist:
    for team2 in team_to_dist:
      match = "CSV;"+team1+";"
      if team1 == team2:
        continue
      if team2 in sim_teams:
        continue
      match += team2 + ";" + str(simulate_match(team_to_dist, team1, team2)) + ";"
      print(match)
    sim_teams.add(team1)


# load the data.
#df = pd.read_csv('hockey_games.csv', skiprows=1, names=['date', 'visitor', 'visitor_goals', 'home', 'home_goals', 'unknown', 'att', 'log', 'notes'])
df = pd.read_csv(sys.stdin, skiprows=1, names=['div','date','time', 'home', 'visitor', 'home_goals', 'visitor_goals'])
# make the date column into a date format.
# df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

df['goal_difference'] = df['home_goals'] - df['visitor_goals']

df['home_win'] = np.where(df['goal_difference'] > 0, 1, 0)
df['home_loss'] = np.where(df['goal_difference'] < 0, 1, 0)

teams_to_diff = {}
for i in df.iterrows():
  home = i[1]['home']
  visitor = i[1]['visitor']
  home_diff = i[1]['goal_difference']
  visitor_diff = (-1)*home_diff
  assert(home_diff + visitor_diff == 0)
  
  if home not in teams_to_diff.keys():
    teams_to_diff[home] = []
  if visitor not in teams_to_diff.keys():
    teams_to_diff[visitor] = []

  teams_to_diff[home].append(home_diff)
  teams_to_diff[visitor].append(visitor_diff)

team_to_dist = {}
for key,value in teams_to_diff.items():
  print(key,value)
  res = get_best_distribution(value)
  team_to_dist[key] = (res[0], res[2])
print(team_to_dist)
# simulate_match(team_to_dist, "Ufa", "DynamoMoskva")
#simulate_match(team_to_dist, "Čerepovec", "Omsk")
#simulate_match(team_to_dist, "Kazaň", "Jekatěrinburg")

simulate_all(team_to_dist)
#TODO podivat se, jestli nejde generovani delat lepe
#TODO diskretni rozlozeni
