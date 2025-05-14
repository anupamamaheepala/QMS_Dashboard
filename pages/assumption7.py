import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 7: Weekend Wait Times", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 7: Wait Times Are Shorter on Weekends")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate average wait times
weekend_df = filtered_df[filtered_df["IS_WEEKEND"] == 1]
weekday_df = filtered_df[filtered_df["IS_WEEKEND"] == 0]
weekend_avg = weekend_df["WAIT_TIME_MIN"].mean()
weekday_avg = weekday_df["WAIT_TIME_MIN"].mean()

# Create bar chart
bar_data = pd.DataFrame({
    "Day Type": ["Weekend", "Weekday"],
    "Average Wait Time (min)": [weekend_avg, weekday_avg]
})
fig = px.bar(bar_data, x="Day Type", y="Average Wait Time (min)", title="Average Wait Time by Day Type")
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("Weekend Avg Wait Time", f"{weekend_avg:.2f} min")