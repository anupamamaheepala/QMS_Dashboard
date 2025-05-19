import streamlit as st

st.set_page_config(page_title="QMS Dashboard", layout="wide")
st.title("Queue Management System Dashboard")
st.markdown("Select a metric to view detailed results and visualizations.")

# Create buttons for each result page
col1, col2 = st.columns(2)
with col1:
    if st.button("Average Wait Time"):
        st.switch_page("pages/avg_wait_time.py")
    if st.button("Average Service Time by Service Type"):
        st.switch_page("pages/avg_service_time_service_type.py")
    if st.button("Total Transactions by Branch"):
        st.switch_page("pages/total_transactions_branch.py")
    if st.button("Peak Hour Transaction Volume"):
        st.switch_page("pages/transactions_by_hour.py")
    if st.button("Percentage of Long Wait Times"):
        st.switch_page("pages/pct_long_wait.py")
with col2:
    if st.button("Average Wait Time by Day of Week"):
        st.switch_page("pages/avg_wait_time_dayofweek.py")
    if st.button("Branch Traffic Utilization"):
        st.switch_page("pages/branch_traffic_utilization.py")
    if st.button("Total Service Time for High-Priority Tokens"):
        st.switch_page("pages/total_service_time_highpriority.py")
    if st.button("Average Wait Time: Weekend vs. Weekday"):
        st.switch_page("pages/avg_wait_time_weekendvsweekday.py")
    if st.button("Customer Type Transaction Share"):
        st.switch_page("pages/customer_type_share.py")

st.markdown("---")
st.write("Use the buttons above to explore metrics. Each page allows filtering by branch location.")