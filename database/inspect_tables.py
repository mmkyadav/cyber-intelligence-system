import sqlite3
import pandas as pd

DB_PATH = "database/cyber_sector.db"

conn = sqlite3.connect(DB_PATH)

print("\n=== RAW TABLE METADATA ===")
try:
    df = pd.read_sql("SELECT * FROM raw_tables", conn)
    print(df)
except Exception as e:
    print("No raw_tables data found")

print("\n=== REGIONS ===")
try:
    df = pd.read_sql("SELECT * FROM regions", conn)
    print(df)
except Exception as e:
    print("No regions data found")

print("\n=== METRICS ===")
try:
    df = pd.read_sql("SELECT * FROM metrics", conn)
    print(df)
except Exception as e:
    print("No metrics data found")

conn.close()