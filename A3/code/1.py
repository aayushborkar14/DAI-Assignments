import matplotlib as mpl
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

mpl.rcParams["figure.dpi"] = 300

df = pd.read_csv("NED21.11.1-D-5.1.1-20111026-v20120814.csv", skiprows=12)
df = df.iloc[:1500]
df = df[df["D (Mpc)"] < 4]
n = len(df)

v = np.histogram(df["D (Mpc)"], bins=10, range=(0, 4))[0]
p = v / n
print("The estimated probabilities for bincount 10 are", p)

plt.hist(df["D (Mpc)"], bins=10, range=(0, 4))
plt.xlabel("Distance (Mpc)")
plt.ylabel("Count")
plt.savefig("10binhistogram.png")


def cross_validation(p, n, h):
    return (2 / ((n - 1) * h)) - ((n + 1) / ((n - 1) * h)) * np.sum(p**2)


J = np.zeros(1000)
for bincount in range(1, 1001):
    v, bins = np.histogram(df["D (Mpc)"], bins=bincount, range=(0, 4))
    p = v / n
    J[bincount - 1] = cross_validation(p, n, bins[1] - bins[0])

plt.close()
plt.plot(list(range(1, 1001)), J)
plt.xlabel("Number of bins")
plt.ylabel("Cross-validation score")
plt.savefig("crossvalidation.png")

optimal_h = np.argmin(J) + 1
print("The optimal bincount is", optimal_h)

plt.hist(df["D (Mpc)"], bins=optimal_h, range=(0, 4))
plt.xlabel("Distance (Mpc)")
plt.ylabel("Count")
plt.savefig("optimalhistogram.png")
