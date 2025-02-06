import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

print (f"my average score is {round(averagescore - par,2)}above par")
print (f"my worst score to par is {worst(scores)-par} shots over par")
print (f"my best score to par is {best(scores)-par} shots over par")

plt.scatter(stats["score"], stats["putts"])
plt.xlabel("score")
plt.ylabel("putts")
plt.title("correlation between score and putts")
plt.show()