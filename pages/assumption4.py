import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 4: Location Transactions", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 4: Majority of Transactions at Location")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate transaction count for Location 21
location_21_count = len(filtered_df[filtered_df["LOCATION_ID"] == 21])

# Transaction distribution by location
location_counts = filtered_df["LOCATION_ID"].value_counts().reset_index()
location_counts.columns = ["LOCATION_ID", "Transaction Count"]

# Create pie chart
fig = px.pie(location_counts, names="LOCATION_ID", values="Transaction Count", title="Transaction Distribution by Location")
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("Location 21 Transaction Count", f"{location_21_count}")