import plotly.graph_objects as go
import pandas as pd

data = {
    "Year": [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017],
    "Strike Rate": [220.55, 182.46, 123.40, 106.54, 116.27, 134.62, 150.66, 116.00],
    "Average Runs": [53.67, 26.00, 33.14, 16.28, 25.00, 83.20, 75.83, 26.36],
    "Total Runs": [161, 104, 232, 114, 200, 416, 455, 290],
}

df = pd.DataFrame(data)

df["angle"] = (df.index / len(df)) * 360

fig = go.Figure()

for stat in ["Strike Rate", "Average Runs", "Total Runs"]:
    fig.add_trace(
        go.Barpolar(
            r=df[stat],
            theta=df["angle"],
            name=stat,
            width=360 / len(df),
            customdata=df["Year"],
            hovertemplate="Year: %{customdata}<br>"
            + stat
            + ": %{r:.2f}<extra></extra>",
        )
    )

fig.update_layout(
    title="MS Dhoni's Batting Statistics by Year",
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[
                0,
                df[["Strike Rate", "Average Runs", "Total Runs"]].values.max() * 1.1,
            ],
        ),
        angularaxis=dict(
            visible=True,
            direction="clockwise",
            tickmode="array",
            tickvals=df["angle"],
            ticktext=df["Year"],
        ),
    ),
    showlegend=True,
)

colors = ["#E63946", "#F1FAEE", "#457B9D"]
for i, trace in enumerate(fig.data):
    trace.update(marker_color=colors[i], opacity=0.8)

fig.show()

