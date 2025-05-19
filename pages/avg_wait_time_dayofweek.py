import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Average Wait Time by Day of Week", layout="wide")
st.title("Average Wait Time by Day of Week")

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

# Calculate average wait time by day of week
avg_wait_day = filtered_data.groupby("DAY_OF_WEEK")["WAIT_TIME_MIN"].mean().reset_index()
# Map day of week numbers to names
day_map = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
avg_wait_day["DAY_OF_WEEK"] = avg_wait_day["DAY_OF_WEEK"].map(day_map)

# Bar chart
fig = px.bar(
    avg_wait_day,
    x="DAY_OF_WEEK",
    y="WAIT_TIME_MIN",
    title="Average Wait Time by Day of Week",
    labels={"WAIT_TIME_MIN": "Average Wait Time (Minutes)", "DAY_OF_WEEK": "Day of Week"}
)
st.plotly_chart(fig, use_container_width=True)

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")