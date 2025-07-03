import re
import pandas as pd
import os

def parse_log_file(filepath):
    pattern = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) .*? (?P<type>TR START|TR END|ANPR FAIL|SU ERROR) .*? passage=(?P<passage_id>\w+) .*? device=(?P<device>\w+)")

    entries = []
    with open(filepath, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                entries.append(match.groupdict())

    return pd.DataFrame(entries)

def analyze_logs(df):
    summary = {}
    summary['Total Entries'] = len(df)
    summary['TR START Count'] = (df['type'] == 'TR START').sum()
    summary['TR END Count'] = (df['type'] == 'TR END').sum()
    summary['ANPR Failures'] = (df['type'] == 'ANPR FAIL').sum()
    summary['SU Errors'] = (df['type'] == 'SU ERROR').sum()
    summary['Unique Devices'] = df['device'].nunique()

    return pd.DataFrame.from_dict(summary, orient='index', columns=['Count'])

def save_summary(summary_df, output_file):
    summary_df.to_csv(output_file)

if __name__ == "__main__":
    log_file_path = "sample_toll_log.txt"  # Replace with your log file
    output_summary_path = "log_summary.csv"

    if os.path.exists(log_file_path):
        df = parse_log_file(log_file_path)
        summary_df = analyze_logs(df)
        save_summary(summary_df, output_summary_path)
        print("Log analysis completed. Summary saved to log_summary.csv")
    else:
        print(f"Log file '{log_file_path}' not found. Please provide a valid file.")
