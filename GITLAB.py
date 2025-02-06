import numpy as np
import pandas as pd

stats = pd.read_csv("Golfstats.csv")

def average(x):
    return (round(sum(x)/len(x),2))

def best(x):
    return min(x)

def worst(x):
    return max(x)

scores = stats["score"].tolist()
putts = stats["putts"].tolist()

roundsplayed = len(scores)

par = 72

averagescore = average(scores)
print (averagescore)

averageputts = average(putts)
print (averageputts)

print(worst(scores))
print(best(scores))
print(worst(putts))
print(best(putts))

