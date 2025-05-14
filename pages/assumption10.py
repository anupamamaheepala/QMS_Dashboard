import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 9: Low-Traffic Total Time", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 9: Low-Traffic Branches Have Shorter Total Times")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate average total times
low_traffic_df = filtered_df[filtered_df["BRANCH_TRAFFIC"] < 5000]
high_traffic_df = filtered_df[filtered_df["BRANCH_TRAFFIC"] >= 5000]
low_traffic_avg = low_traffic_df["TOTAL_TIME_MIN"].mean()
high_traffic_avg = high_traffic_df["TOTAL_TIME_MIN"].mean()

# Create bar chart
bar_data = pd.DataFrame({
    "Traffic Type": ["Low Traffic (<5,000)", "High Traffic (≥5,000)"],
    "Average Total Time (min)": [low_traffic_avg, high_traffic_avg]
})
fig = px.bar(bar_data, x="Traffic Type", y="Average Total Time (min)", title="Average Total Time by Branch Traffic")
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("Low-Traffic Avg Total Time", f"{low_traffic_avg:.2f} min")