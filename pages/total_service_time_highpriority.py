import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Total Service Time for High-Priority Tokens", layout="wide")
st.title("Total Service Time for High-Priority Tokens")

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

# Calculate total service time for high-priority tokens
high_priority_data = filtered_data[filtered_data["TOKEN_PRIORITY"] == 1]
if selected_location == "All":
    total_service_time = high_priority_data.groupby("LOCATION")["SERVICE_TIME_MIN"].sum().reset_index()
    fig = px.bar(
        total_service_time,
        x="LOCATION",
        y="SERVICE_TIME_MIN",
        title="Total Service Time for High-Priority Tokens by Branch",
        labels={"SERVICE_TIME_MIN": "Total Service Time (Minutes)"}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    total_service_time = high_priority_data["SERVICE_TIME_MIN"].sum()
    st.metric(f"Total Service Time for High-Priority Tokens in {selected_location}", f"{total_service_time:.2f} minutes")

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")