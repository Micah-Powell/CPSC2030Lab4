import numpy as np
import pandas as pd

stats = pd.read_csv("Golfstats.csv")

def avgscore(score):
    return (round(sum(score)/len(score),2))

def avgputts(putt):
    return sum(putt)/len(putt)

scores = stats["score"].tolist()
putts = stats["putts"].tolist()
roundsplayed = len(scores)
par = 72
averagescore = avgscore(scores)
print (averagescore)