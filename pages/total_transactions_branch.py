import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Total Transactions by Branch", layout="wide")
st.title("Total Transactions by Branch")

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

# Calculate transactions by branch
if selected_location == "All":
    transactions_by_branch = filtered_data.groupby("LOCATION").size().reset_index(name="Transaction_Count")
    fig = px.pie(
        transactions_by_branch,
        names="LOCATION",
        values="Transaction_Count",
        title="Transaction Distribution by Branch"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    transaction_count = len(filtered_data)
    st.metric(f"Total Transactions for {selected_location}", transaction_count)

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")