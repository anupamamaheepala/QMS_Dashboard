import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Branch Traffic Utilization", layout="wide")
st.title("Branch Traffic Utilization")

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

# Calculate branch traffic utilization
if selected_location == "All":
    transactions = filtered_data.groupby("LOCATION").size()
    traffic = filtered_data.groupby("LOCATION")["BRANCH_TRAFFIC"].max()
    utilization = (transactions / traffic * 100).reset_index(name="Utilization")
    fig = px.bar(
        utilization,
        x="LOCATION",
        y="Utilization",
        title="Branch Traffic Utilization (%)",
        labels={"Utilization": "Utilization (%)"}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    transaction_count = len(filtered_data)
    branch_traffic = filtered_data["BRANCH_TRAFFIC"].max()
    utilization = (transaction_count / branch_traffic * 100) if branch_traffic > 0 else 0
    st.metric(f"Traffic Utilization for {selected_location}", f"{utilization:.2f}%")

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")