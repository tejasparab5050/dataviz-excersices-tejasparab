import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Hospital Dashboard - Main", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("hospital_patient_treatment_dataset.csv")

df = load_data()

df["Treatment Cost"] = pd.to_numeric(df["Treatment Cost"], errors="coerce")
df["Hospital Stay (Days)"] = pd.to_numeric(df["Hospital Stay (Days)"], errors="coerce")
df["Recovery Score"] = pd.to_numeric(df["Recovery Score"], errors="coerce")

st.title("Hospital Patient Treatment Dashboard - Main")

st.markdown("Explore treatment cost, hospital stay, and recovery outcomes across departments, treatment types, and doctors.")

col1, col2, col3 = st.columns(3)

with col1:
    dept = st.selectbox("Select Department", options=["All"] + sorted(df["Department"].unique().tolist()))
with col2:
    treatment = st.selectbox("Select Treatment Type", options=["All"] + sorted(df["Treatment Type"].unique().tolist()))
with col3:
    doctor = st.selectbox("Select Doctor", options=["All"] + sorted(df["Doctor Name"].unique().tolist()))

filtered = df.copy()
if dept != "All":
    filtered = filtered[filtered["Department"] == dept]
if treatment != "All":
    filtered = filtered[filtered["Treatment Type"] == treatment]
if doctor != "All":
    filtered = filtered[filtered["Doctor Name"] == doctor]

st.subheader("Key Metrics")

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Avg Treatment Cost", f"{filtered['Treatment Cost'].mean():.0f}")
with m2:
    st.metric("Avg Hospital Stay", f"{filtered['Hospital Stay (Days)'].mean():.1f}")
with m3:
    st.metric("Avg Recovery Score", f"{filtered['Recovery Score'].mean():.1f}")

st.markdown("---")

c1, c2 = st.columns(2)

with c1:
    dept_cost = filtered.groupby("Department", as_index=False)["Treatment Cost"].mean()
    fig1 = px.bar(dept_cost, x="Department", y="Treatment Cost", color="Treatment Cost", title="Cost by Department")
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    treatment_recovery = filtered.groupby("Treatment Type", as_index=False)["Recovery Score"].mean()
    fig2 = px.bar(treatment_recovery, x="Treatment Type", y="Recovery Score", color="Recovery Score", title="Recovery by Treatment Type")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

fig3 = px.scatter(
    filtered,
    x="Treatment Cost",
    y="Recovery Score",
    color="Department",
    hover_data=["Treatment Type", "Doctor Name"],
    title="Cost vs Recovery"
)
st.plotly_chart(fig3, use_container_width=True)
