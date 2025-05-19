import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Average Wait Time", layout="wide")
st.title("Average Wait Time")

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

# Calculate average wait time
avg_wait_time = filtered_data["WAIT_TIME_MIN"].mean()

# Display metric
st.metric("Average Wait Time (Minutes)", f"{avg_wait_time:.2f}")

# Bar chart by location
if selected_location == "All":
    avg_wait_by_location = data.groupby("LOCATION")["WAIT_TIME_MIN"].mean().reset_index()
    fig = px.bar(
        avg_wait_by_location,
        x="LOCATION",
        y="WAIT_TIME_MIN",
        title="Average Wait Time by Branch",
        labels={"WAIT_TIME_MIN": "Average Wait Time (Minutes)", "LOCATION": "Branch"}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write(f"Showing data for {selected_location} only.")

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")