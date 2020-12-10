#! /bin/bash

bet = 100
odds = 3 # 2:1
while odds > 1:
  win=odds*bet
  pure_win=win-bet
  opp_odds=1/(1-1/odds)
  print("Odds:", odds, " win:", win, "opp odds:",opp_odds)

  while opp_odds > 1.0:
    min_hedge_bet = bet/(opp_odds-1)
    if (pure_win+pure_win/2 <= min_hedge_bet):
      break
    print("\tHedge - opp_odds:",opp_odds, "Minimal hedge bet:", min_hedge_bet, " diff", min_hedge_bet*opp_odds-bet-min_hedge_bet, " orig bet ", pure_win-min_hedge_bet)
    opp_odds = opp_odds-0.1

  odds = odds - 0.1
