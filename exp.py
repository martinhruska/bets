#! /usr/bin/python3
import matplotlib.pyplot as plt
import random


mu = 0.5
sigma = 0.2

bets = 1000
runs_count = 100
x = range(0,bets)
runs = []
g = [1]*(bets)
odds = 2.5
delta = 0.2
win_prob = 1/(1+odds-delta)

for j in range(0,runs_count):
  y = [1]*(bets)
  for i in range(0,bets):
    y[i] = y[i-1] + (odds*1 if win_prob >= random.uniform(0,1) else -1)
    g[i] = g[i-1] + (odds*1 if win_prob >= random.gauss(mu,sigma) else -1)
  runs.append(y)

positive_end=len([l[-1] for l in runs if l[-1]>=0])
positive_all=len([x for l in runs for x in l if x >= 0])
print(positive_end/runs_count, positive_all/(runs_count*bets))

plt.figure(0)
plt.rcParams.update({'font.size': 14})
plt.xlabel("Bets")
plt.ylabel("Profit")
for y in runs:
  plt.plot(x,y)
#plt.plot(x,g)

#plt.figure(1)
#plt.hist([random.gauss(mu,sigma) for x in range(0,2*bets)],bins=100)
plt.figure(1)
plt.hist([item for l in runs for item in l],bins=200)
plt.show()
