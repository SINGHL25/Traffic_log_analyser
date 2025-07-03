# Traffic Log Analyzer 🚦

A Python-based tool to parse and analyze roadside toll transaction logs. Helps Intelligent Transport System (ITS) engineers detect issues like ANPR failures or SU communication errors.

## 🔍 Features

- Extracts and summarizes events like:
  - TR START / TR END
  - ANPR FAIL
  - SU ERROR
- Outputs a clean summary CSV
- Built for real-world tolling log formats
- Lightweight and extendable

# 🚦 Toll Log Analyzer using Streamlit

This project is a **log analysis and visualization web app** built using **Python** and **Streamlit**. It parses raw tolling system logs (e.g., from `CoreCallback.cpp`) to extract log events like `VP2`, `VS`, `OIR`, `FTP`, etc., and provides a dashboard to analyze and visualize the log type frequency.

---

## 📂 Features

- 📥 Upload raw `.txt` or `.log` toll system log files
- 🧠 Extracts:
  - Log type (e.g., `VP2`, `VS`)
  - Object ID (e.g., `ID:715`)
  - Details like vehicle dimensions or exit info
- 📊 Interactive bar chart showing log type frequency
- 📋 Data table preview of extracted results
- ✅ Built with `Streamlit`, `Pandas`, and optionally `Matplotlib`

---

## 🖼️ Sample Screenshot

![sample-ui](./screenshot.png)

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt

