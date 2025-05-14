import streamlit as st

# Set page configuration
st.set_page_config(page_title="QMS Dashboard", layout="wide")

# Title
st.title("Queue Management System Dashboard")

# Introduction
st.markdown("""
This dashboard analyzes the QMS dataset to validate key assumptions about wait times, service times, and branch performance.
Select an assumption from the sidebar or click a button below to explore.
""")

# Buttons for each assumption
st.subheader("Explore Assumptions")
col1, col2 = st.columns(2)

with col1:
    if st.button("Assumption 1: High-Traffic Branch Wait Times"):
        st.switch_page("pages/assumption1.py")
    if st.button("Assumption 2: Services and Service Time"):
        st.switch_page("pages/assumption2.py")
    if st.button("Assumption 3: Peak Hours Wait Times"):
        st.switch_page("pages/assumption3.py")
    if st.button("Assumption 4: Location 21 Transactions"):
        st.switch_page("pages/assumption4.py")
    if st.button("Assumption 5: Wait Time Overestimation"):
        st.switch_page("pages/assumption5.py")

with col2:
    if st.button("Assumption 6: Account_Opening Service Time"):
        st.switch_page("pages/assumption6.py")
    if st.button("Assumption 7: Weekend Wait Times"):
        st.switch_page("pages/assumption7.py")
    if st.button("Assumption 8: High-Priority Wait Times"):
        st.switch_page("pages/assumption8.py")
    if st.button("Assumption 9: Low-Traffic Total Time"):
        st.switch_page("pages/assumption9.py")
    if st.button("Assumption 10: Digital_Products Variance"):
        st.switch_page("pages/assumption10.py")

# Note
st.markdown("""
**Note**: You can also navigate to each assumption using the sidebar menu.
The dataset (QMS_dataset.csv) must be in the same directory as dashboard.py.
""")