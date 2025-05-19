import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Average Service Time by Service Type", layout="wide")
st.title("Average Service Time by Service Type")

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

# Calculate average service time by service type
avg_service_time = filtered_data.groupby("SERVICE_TYPE")["SERVICE_TIME_MIN"].mean().reset_index()

# Bar chart
fig = px.bar(
    avg_service_time,
    x="SERVICE_TYPE",
    y="SERVICE_TIME_MIN",
    title="Average Service Time by Service Type",
    labels={"SERVICE_TIME_MIN": "Average Service Time (Minutes)", "SERVICE_TYPE": "Service Type"}
)
st.plotly_chart(fig, use_container_width=True)

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")