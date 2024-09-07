import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

plt.rcParams["figure.dpi"] = 300

df = pd.read_csv("Consumer_Complaints.csv")
df.to_csv("Consumer.csv")
df = df["Product"].value_counts().reset_index()
df.columns = ["Product", "Count"]
df.set_index("Product", inplace=True)
df.head()

# Sort the DataFrame by 'Count' in descending order
df = df.sort_values(by="Count", ascending=False)
df["cumpercentage"] = df["Count"].cumsum() / df["Count"].sum() * 100

fig, ax = plt.subplots(figsize=(15, 8))

ax.bar(df.index, df["Count"], color="C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0", labelsize=12)
ax2.tick_params(axis="y", colors="C1", labelsize=12)

ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(df.index, rotation=45, ha="right", fontsize=12)
plt.subplots_adjust(bottom=0.2)

ax.set_xlabel("Categories", fontsize=14)
ax.set_ylabel("Count", color="C0", fontsize=14)
ax2.set_ylabel("Cumulative Percentage", color="C1", fontsize=14)
plt.title("Count and Cumulative Percentage by Category", fontsize=16)

plt.savefig("pareto.png", bbox_inches="tight")
plt.show()
