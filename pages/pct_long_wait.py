import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Percentage of Long Wait Times", layout="wide")
st.title("Percentage of Long Wait Times (>15 Minutes)")

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

# Calculate percentage of long wait times
if selected_location == "All":
    long_wait = filtered_data[filtered_data["WAIT_TIME_MIN"] > 15].groupby("LOCATION").size()
    total = filtered_data.groupby("LOCATION").size()
    pct_long_wait = (long_wait / total * 100).reset_index(name="Percentage")
    fig = px.bar(
        pct_long_wait,
        x="LOCATION",
        y="Percentage",
        title="Percentage of Transactions with Wait Time >15 Minutes by Branch",
        labels={"Percentage": "% of Transactions"}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    long_wait_count = len(filtered_data[filtered_data["WAIT_TIME_MIN"] > 15])
    total_count = len(filtered_data)
    pct = (long_wait_count / total_count * 100) if total_count > 0 else 0
    st.metric(f"Percentage of Long Wait Times for {selected_location}", f"{pct:.2f}%")

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")