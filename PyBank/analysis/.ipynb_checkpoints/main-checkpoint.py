import os
import csv
import pandas as pd


budget_df = pd.read_csv('python-challenge', 'PyBank', 'Resources', 'budget_data (1).csv')

totmos = budget_df["Date"].count()

profit_loss = budget_df["Profit/Losses"].sum()

avgchg = [0]
pl_chg = budget_df["Profit/Losses"].to_list()
for x in range(1,len(pl_chg)):
    diff = pl_chg[x] - pl_chg[x - 1]
    avgchg.append(diff)
avgchg

x = budget_df["Differences"].sum() / (len(avgchg)-1)
x = round(x, 2)

budget_df[budget_df["Differences"]==budget_df["Differences"].max()].Date.item()

budget_df["Differences"].max()

budget_df["Differences"].min()

budget_df = pd.read_csv("Resources/budget_data (1).csv")

print("Financial Analysis")
print("-------------------------")
print(f'Total Months: {len(budget_df)}')
print(f'Total: ${budget_df["Profit/Losses"].sum()}')
print(f'Average Change: ${x}')
print(f'Greatest Increase in Profits: {budget_df[budget_df["Differences"]==budget_df["Differences"].max()].Date.item()} (${budget_df["Differences"].max()})')
print(f'Greatest Decrease in Profits: {budget_df[budget_df["Differences"]==budget_df["Differences"].min()].Date.item()} (${budget_df["Differences"].min()})')






