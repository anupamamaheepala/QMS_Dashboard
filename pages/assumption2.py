import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Assumption 2: Services and Service Time", layout="wide")

# Load dataset
df = pd.read_csv("../QMS_dataset.csv")

# Title
st.title("Assumption 2: Services and Service Time")

# Sidebar filters
st.sidebar.header("Filters")
location_ids = df["LOCATION_ID"].unique()
selected_locations = st.sidebar.multiselect("Select Location ID", location_ids, default=list(location_ids))
language_ids = df["LANGUAGE_ID"].unique()
selected_languages = st.sidebar.multiselect("Select Language ID", language_ids, default=list(language_ids))

# Filter dataset
filtered_df = df[df["LOCATION_ID"].isin(selected_locations) & df["LANGUAGE_ID"].isin(selected_languages)]

# Calculate average service time by service type
service_time_avg = filtered_df.groupby("SERVICE_TYPE")["SERVICE_TIME_MIN"].mean().reset_index()

# Highlight Withdrawal_Deposit
withdrawal_deposit_avg = service_time_avg[service_time_avg["SERVICE_TYPE"] == "Withdrawal_Deposit"]["SERVICE_TIME_MIN"].iloc[0] if "Withdrawal_Deposit" in service_time_avg["SERVICE_TYPE"].values else 0

# Create bar chart
fig = px.bar(service_time_avg, x="SERVICE_TYPE", y="SERVICE_TIME_MIN", title="Average Service Time by Service Type")
fig.update_traces(marker_color=["#FF4B4B" if x == "Withdrawal_Deposit" else "#1F77B4" for x in service_time_avg["SERVICE_TYPE"]])
st.plotly_chart(fig, use_container_width=True)

# Display metric
st.metric("Withdrawal_Deposit Avg Service Time", f"{withdrawal_deposit_avg:.2f} min")