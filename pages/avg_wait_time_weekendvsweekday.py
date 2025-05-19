import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Average Wait Time: Weekend vs. Weekday", layout="wide")
st.title("Average Wait Time: Weekend vs. Weekday")

# Load data
qms_data = pd.read_csv("data/QMS_dataset.csv")
location_data = pd.read_csv("data/location.csv")
data = qms_data.merge(location_data, on="LOCATION_ID", how="left")

# Filter by LOCATION_ID
locations = data[["LOCATION_ID", "LOCATION"]].drop_duplicates().sort_values("LOCATION")
location_options = ["All"] + locations["LOCATION"].tolist()
selected_location = st.selectbox("Select Branch Location", location_options)

# Apply filter
if selected_location != "All":
    location_id = locations[locations["LOCATION"] == selected_location]["LOCATION_ID"].iloc[0]
    filtered_data = data[data["LOCATION_ID"] == location_id]
else:
    filtered_data = data

# Calculate average wait time by weekend/weekday
avg_wait_weekend = filtered_data.groupby("IS_WEEKEND")["WAIT_TIME_MIN"].mean().reset_index()
avg_wait_weekend["IS_WEEKEND"] = avg_wait_weekend["IS_WEEKEND"].map({0: "Weekday", 1: "Weekend"})

# Bar chart
fig = px.bar(
    avg_wait_weekend,
    x="IS_WEEKEND",
    y="WAIT_TIME_MIN",
    title="Average Wait Time: Weekend vs. Weekday",
    labels={"WAIT_TIME_MIN": "Average Wait Time (Minutes)", "IS_WEEKEND": "Day Type"}
)
st.plotly_chart(fig, use_container_width=True)

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")