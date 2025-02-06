import numpy as np
import pandas as pd

stats = pd.read_csv("Golfstats.csv")

def avgscore(score):
    return sum(score)/len(score)

def avgputts(putt):
    return sum(putt)/len(putt)

scores = stats["score"]
putts = []
roundsplayed = 0

print (scores)


