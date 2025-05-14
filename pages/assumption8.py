import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Assumption 8: High-Priority Wait Times", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 8: High-Priority Tokens Have Shorter Wait Times")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.texture.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate average wait time for high-priority tokens
high_priority_df = filtered_df[filtered_df["TOKEN_PRIORITY"] == 1]
high_priority_avg = high_priority_df["WAIT_TIME_MIN"].mean()

# Display metric
st.metric("High-Priority Avg Wait Time", f"{high_priority_avg:.2f} min")

# Note
st.markdown("**Note**: All tokens in the dataset have TOKEN_PRIORITY = 1, so this metric reflects the overall average wait time.")