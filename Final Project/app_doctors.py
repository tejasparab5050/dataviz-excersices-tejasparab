import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Hospital Dashboard - Doctors", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("hospital_patient_treatment_dataset.csv")

df = load_data()

df["Treatment Cost"] = pd.to_numeric(df["Treatment Cost"], errors="coerce")
df["Hospital Stay (Days)"] = pd.to_numeric(df["Hospital Stay (Days)"], errors="coerce")
df["Recovery Score"] = pd.to_numeric(df["Recovery Score"], errors="coerce")

st.title("Doctor Performance Dashboard")

doctor = st.selectbox("Select Doctor", sorted(df["Doctor Name"].unique().tolist()))

filtered = df[df["Doctor Name"] == doctor]

st.subheader(f"Performance Summary for {doctor}")

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Avg Treatment Cost", f"{filtered['Treatment Cost'].mean():.0f}")
with m2:
    st.metric("Avg Hospital Stay", f"{filtered['Hospital Stay (Days)'].mean():.1f}")
with m3:
    st.metric("Avg Recovery Score", f"{filtered['Recovery Score'].mean():.1f}")

st.markdown("---")

fig1 = px.histogram(filtered, x="Treatment Cost", nbins=20, title="Treatment Cost Distribution")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(filtered, x="Recovery Score", nbins=20, title="Recovery Score Distribution")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    filtered,
    x="Treatment Cost",
    y="Recovery Score",
    color="Treatment Type",
    title="Cost vs Recovery (Doctor View)"
)
st.plotly_chart(fig3, use_container_width=True)
