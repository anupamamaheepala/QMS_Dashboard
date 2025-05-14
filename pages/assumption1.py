import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 1: High-Traffic Wait Times", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 1: High-Traffic Branches Have Higher Wait Times")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate average wait times
high_traffic_df = filtered_df[filtered_df["BRANCH_TRAFFIC"] > 10000]
low_traffic_df = filtered_df[filtered_df["BRANCH_TRAFFIC"] <= 10000]
high_traffic_avg = high_traffic_df["WAIT_TIME_MIN"].mean()
low_traffic_avg = low_traffic_df["WAIT_TIME_MIN"].mean()

# Create bar chart
bar_data = pd.DataFrame({
    "Traffic Type": ["High Traffic (>10,000)", "Low Traffic (≤10,000)"],
    "Average Wait Time (min)": [high_traffic_avg, low_traffic_avg]
})
fig = px.bar(bar_data, x="Traffic Type", y="Average Wait Time (min)", title="Average Wait Time by Branch Traffic")
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("High-Traffic Avg Wait Time", f"{high_traffic_avg:.2f} min")