import re
import pandas as pd
import os

def parse_log_file(filepath):
    # Match lines that contain actual log data like /I/VP2: ID:715 ...
    pattern = re.compile(
        r"/[A-Z]/(?P<log_type>\w+): ID:(?P<id>\d+)\s*(?P<details>[^/]*)/0h:\(",
        re.IGNORECASE
    )

    entries = []

    with open(filepath, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                entries.append(match.groupdict())

    return pd.DataFrame(entries)

def analyze_logs(df):
    if df.empty:
        print("⚠️ No valid log entries parsed.")
        return pd.DataFrame()

    summary = {
        "Total Entries": len(df),
        "Unique Log Types": df['log_type'].nunique(),
        "Unique IDs": df['id'].nunique(),
        "Log Type Counts": df['log_type'].value_counts().to_dict()
    }

    return pd.DataFrame.from_dict(summary, orient='index', columns=["Value"])

def save_summary(summary_df, output_file):
    summary_df.to_csv(output_file)

if __name__ == "__main__":
    log_file_path = ")20250529142906.653000VDCMGCoreCall.txt"  # Your log file
    output_summary_path = "log_summary.csv"

    if os.path.exists(log_file_path):
        df = parse_log_file(log_file_path)
        print(df.head())  # Debug: show what was parsed
        summary_df = analyze_logs(df)
        save_summary(summary_df, output_summary_path)
        print("✅ Log analysis completed. Summary saved to log_summary.csv")
    else:
        print(f"❌ Log file '{log_file_path}' not found.")

import matplotlib.pyplot as plt

def visualize_log_counts(df):
    if df.empty:
        print("⚠️ No data to visualize.")
        return

    counts = df['log_type'].value_counts()
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Log Type Frequency")
    plt.xlabel("Log Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("log_type_counts.png")
    plt.show()
    visualize_log_counts(df)
