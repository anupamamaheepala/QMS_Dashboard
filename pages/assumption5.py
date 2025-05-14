import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 5: Wait Time Overestimation", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 5: Estimated Wait Time Is Overestimated")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate overestimation
filtered_df["Wait_Time_Diff"] = filtered_df["ESTIMATED_WAITING_TIME"] - filtered_df["WAIT_TIME_MIN"]
avg_overestimation = filtered_df["Wait_Time_Diff"].mean()

# Create histogram
fig = px.histogram(filtered_df, x="Wait_Time_Diff", title="Distribution of Wait Time Estimation Differences")
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("Average Wait Time Overestimation", f"{avg_overestimation:.2f} min")