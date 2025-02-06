import numpy as np
import pandas as pd

stats = pd.read_csv("Golfstats.csv")

def avgscore(score):
    return sum(score)/len(score)

def avgputts(putt):
    return sum(putt)/len(putt)

scores = stats["score"].tolist()
putts = stats["putts"].tolist()
roundsplayed = 0

print (putts)

