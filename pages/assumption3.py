import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 3: Peak Hours Wait Times", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 3: Wait Times Are Longer During Peak Hours (9 AM–12 PM)")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate average wait times
peak_hours_df = filtered_df[filtered_df["HOUR_OF_DAY"].between(9, 12)]
non_peak_hours_df = filtered_df[~filtered_df["HOUR_OF_DAY"].between(9, 12)]
peak_hours_avg = peak_hours_df["WAIT_TIME_MIN"].mean()
non_peak_hours_avg = non_peak_hours_df["WAIT_TIME_MIN"].mean()

# Create bar chart
bar_data = pd.DataFrame({
    "Time Period": ["Peak Hours (9 AM–12 PM)", "Non-Peak Hours"],
    "Average Wait Time (min)": [peak_hours_avg, non_peak_hours_avg]
})
fig = px.bar(bar_data, x="Time Period", y="Average Wait Time (min)", title="Average Wait Time by Time Period")
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("Peak Hours Avg Wait Time", f"{peak_hours_avg:.2f} min")