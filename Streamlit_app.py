import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

st.set_page_config(page_title="Log Parser Dashboard", layout="wide")
st.title("📊 Log Type Frequency Dashboard")

# --- Function to parse log file ---
def parse_log_file(filepath):
    pattern = re.compile(r"/[A-Z]/(?P<log_type>\w+): ID:(?P<id>\d+)\s*(?P<details>[^/]*)/0h:\(", re.IGNORECASE)
    entries = []

    with open(filepath, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                entries.append(match.groupdict())

    return pd.DataFrame(entries)

# --- Upload and parse ---
uploaded_file = st.file_uploader("Upload a raw log file", type=["txt", "log"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8").splitlines()
    with open("temp_log.txt", "w") as f:
        for line in content:
            f.write(line + "\n")

    df = parse_log_file("temp_log.txt")

    if not df.empty:
        st.success(f"Parsed {len(df)} log entries ✅")

        st.subheader("Log Type Counts")
        log_type_counts = df['log_type'].value_counts()

        st.bar_chart(log_type_counts)

        st.subheader("Raw Parsed Data")
        st.dataframe(df.head(50))
    else:
        st.warning("No valid log entries found in file.")
