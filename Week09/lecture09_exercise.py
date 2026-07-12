"""
Lecture 9 Exercise — World Happiness Dashboard
================================================
Run with: streamlit run lecture09_exercise.py

Dashboard purpose (REQUIRED — write this before any code):
# PURPOSE: Help users explore how happiness varies across countries and what factors contribute to it.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\Tejas Parab\OneDrive\UE\Data Visualization\Week09\world_happiness_2023.csv")




df.columns = ['Country','Region','Score','GDP','Social_Support',
              'Life_Expectancy','Freedom','Generosity','Corruption']

st.set_page_config(page_title="World Happiness Dashboard", page_icon="🌍", layout="wide")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 1: Title and caption
# ─────────────────────────────────────────────────────────────────────────────
st.title("🌍 World Happiness Dashboard")
st.caption("Explore global happiness scores and key contributing factors for 2023.")

# ─────────────────────────────────────────────────────────────────────────────
# TASK 2: Sidebar filters
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Filters")

    regions = ["All"] + sorted(df["Region"].unique())
    selected_region = st.selectbox("Select Region", regions)

    top_n = st.slider("Top N Countries", 5, 30, 15)

filtered = df.copy()
if selected_region != "All":
    filtered = filtered[filtered["Region"] == selected_region]

filtered = filtered.sort_values("Score", ascending=False).head(top_n)

# ─────────────────────────────────────────────────────────────────────────────
# TASK 3: KPI row
# ─────────────────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric("Countries Shown", len(filtered))

global_avg = df["Score"].mean()
current_avg = filtered["Score"].mean()
delta = round(current_avg - global_avg, 3)

col2.metric("Average Happiness Score", round(current_avg, 3), delta)

happiest = filtered.iloc[0]["Country"]
col3.metric("Happiest Country", happiest)

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# TASK 4: Two charts
# ─────────────────────────────────────────────────────────────────────────────
left, right = st.columns([2, 1])

# LEFT — Horizontal bar chart
bar_fig = px.bar(
    filtered.sort_values("Score"),
    x="Score",
    y="Country",
    orientation="h",
    color="Score",  # COLOUR TYPE: sequential
    color_continuous_scale="Blues"
)

bar_fig.update_layout(
    title="Top Countries by Happiness Score",
    xaxis_title="Happiness Score",
    yaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial"),
)
bar_fig.update_xaxes(range=[0, filtered["Score"].max() + 0.2])

left.plotly_chart(bar_fig, use_container_width=True)

# RIGHT — Scatter GDP vs Score
scatter_fig = px.scatter(
    filtered,
    x="GDP",
    y="Score",
    size="Social_Support",
    color="Region",  # COLOUR TYPE: categorical
    hover_name="Country"
)

scatter_fig.update_layout(
    title="GDP vs Happiness Score",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial"),
)

right.plotly_chart(scatter_fig, use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# EXTENSION — Diverging colour scale chart
# ─────────────────────────────────────────────────────────────────────────────
df["Freedom_Diff"] = df["Freedom"] - df["Freedom"].mean()

div_fig = px.bar(
    df.sort_values("Freedom_Diff"),
    x="Freedom_Diff",
    y="Country",
    orientation="h",
    color="Freedom_Diff",  # COLOUR TYPE: diverging
    color_continuous_scale="RdBu",
)

div_fig.update_layout(
    title="Freedom Score Difference from Global Average",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial"),
)

# FIXED ANNOTATION — place above chart
div_fig.add_annotation(
    x=0,
    yref="paper",
    y=1.05,
    text="Midpoint = Global Average Freedom",
    showarrow=False,
    font=dict(size=12)
)

st.plotly_chart(div_fig, use_container_width=True)
