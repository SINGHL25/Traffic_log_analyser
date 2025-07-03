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

## 📁 Sample Log Format

```
2025-06-30 08:01:15 INFO TR START lane=3 passage=TP03 device=SU01
2025-06-30 08:01:20 WARN ANPR FAIL lane=3 passage=TP03 device=ANPR03
2025-06-30 08:01:45 INFO TR END lane=3 passage=TP03 device=SU01
2025-06-30 08:03:00 ERROR SU ERROR lane=3 passage=TP04 device=SU02
```

## ⚙️ How to Run

1. Clone this repo
2. Add your log file as `sample_toll_log.txt`
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the analyzer:
   ```
   python traffic_log_analyzer.py
   ```

Output will be saved to: `log_summary.csv`

## 📊 Output Example

| Event Type      | Count |
|-----------------|-------|
| TR START Count  | 10    |
| TR END Count    | 10    |
| ANPR Failures   | 3     |
| SU Errors       | 1     |
| Unique Devices  | 4     |

## 🔧 Skills Practiced

- Python
- Regex
- DataFrame analysis (Pandas)
- Real-world ITS log understanding

## 👨‍💻 Author

Designed by an ITS Support Engineer for real-world RCA simulation. Ready to demonstrate in interviews or automation tests.
