import os
import re
import sqlite3
import camelot
import pandas as pd
from tqdm import tqdm

PDF_PATH = "cyber_ireland_2022.pdf"
DB_PATH = "database/cyber_sector.db"
SCHEMA_PATH = "database/schema.sql"


def initialize_database():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    return conn


def clean_column_name(col):
    col = str(col).strip()
    col = re.sub(r"\s+", "_", col)
    col = re.sub(r"[^\w_]", "", col)
    return col.lower()


def normalize_dataframe(df):
    df.columns = [clean_column_name(col) for col in df.columns]
    df = df.dropna(how="all")
    df = df.fillna("")
    return df


def store_table_metadata(conn, table_name, page, df):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO raw_tables (table_name, page_number, row_count, column_count)
        VALUES (?, ?, ?, ?)
        """,
        (table_name, page, len(df), len(df.columns)),
    )
    conn.commit()


def extract_tables():
    print("Extracting tables from PDF...")

    tables = camelot.read_pdf(
        PDF_PATH,
        pages="all",
        flavor="lattice"
    )

    print(f"Total tables found: {tables.n}")

    conn = initialize_database()

    for i, table in tqdm(enumerate(tables), total=tables.n):
        df = normalize_dataframe(table.df)

        table_name = f"table_{i+1}"
        page_number = table.page

        store_table_metadata(conn, table_name, page_number, df)

    conn.close()

    print("Raw table metadata stored successfully.")


if __name__ == "__main__":
    extract_tables()