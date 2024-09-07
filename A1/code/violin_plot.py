import plotly.graph_objects as go
import numpy as np
import pandas as pd

np.random.seed(69)

branches = ["CSE", "EE", "MEMS", "Math", "Profs"]
num_ratings_per_branch = 1000

data = []
for branch in branches:
    if branch == "CSE":
        ratings = np.clip(np.random.normal(2.2, 0.25, num_ratings_per_branch), 1, 5)
    elif branch == "EE":
        ratings = np.clip(np.random.normal(3.8, 0.45, num_ratings_per_branch), 1, 5)
    elif branch == "MEMS":
        ratings = np.clip(np.random.normal(3.3, 0.2, num_ratings_per_branch), 1, 5)
    elif branch == "Math":
        ratings = np.clip(np.random.normal(3.0, 0.44, num_ratings_per_branch), 1, 5)
    else:
        ratings = np.clip(np.random.normal(4.5, 0.7, num_ratings_per_branch), 1, 5)

    data.extend([(branch, rating) for rating in ratings])

df = pd.DataFrame(data, columns=["Branch", "Safe Rating"])

fig = go.Figure()

for branch in branches:
    subset = df[df["Branch"] == branch]
    fig.add_trace(
        go.Violin(
            x=subset["Branch"],
            y=subset["Safe Rating"],
            name=branch,
            box_visible=True,
            meanline_visible=True,
            points="all",
        )
    )

fig.update_layout(
    title="Safe App Review across branches (parody)",
    xaxis_title="Branch",
    yaxis_title="Safe Rating",
    violinmode="group",
    yaxis_range=[0.5, 5.5],
)

fig.show()

