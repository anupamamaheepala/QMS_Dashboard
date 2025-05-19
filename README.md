[Install required Python packages]
    pip install streamlit pandas plotly

[Run the app]
    streamlit run dashboard.py

[File Structure]
    project/
    │
    ├── data/
    │   ├── QMS_dataset.csv
    │   ├── location.csv
    │
    ├── pages/
    │   ├── avg_wait_time.py
    │   ├── avg_service_time_service_type.py
    │   ├── total_transactions_branch.py
    │   ├── transactions_by_hour.py
    │   ├── pct_long_wait.py
    │   ├── avg_wait_time_dayofweek.py
    │   ├── branch_traffic_utilization.py
    │   ├── total_service_time_highpriority.py
    │   ├── avg_wait_time_weekendvsweekday.py
    │   ├── customer_type_share.py
    │
    ├── dashboard.py