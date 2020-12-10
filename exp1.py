#! /bin/bash

bet = 100
odds = 2 # 2:1
while odds > 1:
  win=odds*bet
  print("Odds:", odds, " win:", win)
  for i in range(int(odds*10)-10-1,-1,-1):
    opp_odds=1/(1-1/(odds-i/10.0))
    hedge_bet=2*bet/opp_odds
    diff=win-bet-hedge_bet
    print("\tHedge odds:",opp_odds, "bet:", hedge_bet, " diff", diff)
    if (diff < 0):
      break
  odds = odds - 0.1
