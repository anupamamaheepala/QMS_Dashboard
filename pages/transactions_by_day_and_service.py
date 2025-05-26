import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Transactions by Day of Week and Service Type", layout="wide")
st.title("Transactions by Day of Week and Service Type")

# Load data
qms_data = pd.read_csv("data/QMS_dataset.csv")
location_data = pd.read_csv("data/location.csv")
data = qms_data.merge(location_data, on="LOCATION_ID", how="left")

# Clean data: Remove invalid rows
data = data.dropna(subset=["SERVICE_TYPE", "DAY_OF_WEEK", "LOCATION"])
data = data[data["WAIT_TIME_MIN"] >= 0]

# Map DAY_OF_WEEK to day names
day_mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
data["DAY_NAME"] = data["DAY_OF_WEEK"].map(day_mapping)

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

# Calculate transaction counts by day and service type
transaction_counts = filtered_data.groupby(["DAY_NAME", "SERVICE_TYPE"]).size().reset_index(name="Transaction_Count")

# Pivot for grouped bar chart
pivot_data = transaction_counts.pivot(index="DAY_NAME", columns="SERVICE_TYPE", values="Transaction_Count").fillna(0)
pivot_data = pivot_data.reset_index()

# Find the day and service type with the highest transaction count
most_common = transaction_counts.loc[transaction_counts["Transaction_Count"].idxmax()]
most_common_day = most_common["DAY_NAME"]
most_common_service = most_common["SERVICE_TYPE"]
most_common_count = most_common["Transaction_Count"]

# Create grouped bar chart
fig = go.Figure()
for service_type in pivot_data.columns[1:]:  # Skip DAY_NAME column
    fig.add_trace(
        go.Bar(
            x=pivot_data["DAY_NAME"],
            y=pivot_data[service_type],
            name=service_type,
        )
    )

fig.update_layout(
    barmode="group",
    title="Transaction Distribution by Day of Week and Service Type",
    xaxis_title="Day of Week",
    yaxis_title="Number of Transactions",
    legend_title="Service Type",
    template="plotly_white",
)

st.plotly_chart(fig, use_container_width=True)

# Display metric for highest transaction day-service combination
st.metric(
    f"Highest Transaction Volume for {selected_location}",
    f"Day: {most_common_day}, Service: {most_common_service} ({most_common_count} transactions)"
)

# Back to Dashboard button
if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")