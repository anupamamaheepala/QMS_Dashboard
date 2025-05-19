import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Type Transaction Share", layout="wide")
st.title("Customer Type Transaction Share")

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

# Calculate customer type share
customer_type_share = filtered_data.groupby("CUSTOMER_TYPE_ID").size().reset_index(name="Transaction_Count")
customer_type_share["Percentage"] = customer_type_share["Transaction_Count"] / customer_type_share["Transaction_Count"].sum() * 100

# Pie chart
fig = px.pie(
    customer_type_share,
    names="CUSTOMER_TYPE_ID",
    values="Percentage",
    title="Transaction Share by Customer Type",
    labels={"CUSTOMER_TYPE_ID": "Customer Type", "Percentage": "% of Transactions"}
)
st.plotly_chart(fig, use_container_width=True)

if st.button("Back to Dashboard"):
    st.switch_page("dashboard.py")