import os
import csv
import pandas as pd
from collections import Counter

df = pd.read_csv("Resources/election_data.csv")

len(df)

df["Candidate"].unique()

cand_per = []
for i in df["Candidate"].unique():
    n = len(df[df["Candidate"] == i]) / len(df)
    cand_per.append(round(n*100, 2))
cand_per

df["Candidate"].value_counts()

vote = df["Candidate"]

cand_votes = Counter(vote)

winner = max(df["Candidate"].value_counts())


most_votes = max(cand_votes.values())

First = [i for i in cand_votes.keys() 
       if cand_votes[i]==most_votes]

sorted(First)