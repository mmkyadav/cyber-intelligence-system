import sqlite3

DB_PATH = "database/cyber_sector.db"


def insert_region(conn, region_name, region_type):
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO regions (region_name, region_type)
        VALUES (?, ?)
        """,
        (region_name, region_type),
    )


def insert_metric(conn, metric_name, region, category, year, value, source):
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO metrics (metric_name, region, category, year, value, source)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (metric_name, region, category, year, value, source),
    )


def build_metrics():

    conn = sqlite3.connect(DB_PATH)

    # -------------------------
    # Regions
    # -------------------------

    insert_region(conn, "Ireland", "National")
    insert_region(conn, "Cork", "NUTS3")
    insert_region(conn, "Kerry", "NUTS3")
    insert_region(conn, "South-West", "Aggregated")

    # -------------------------
    # Firm Metrics
    # -------------------------

    insert_metric(
        conn,
        "firm_count",
        "Ireland",
        "total",
        2021,
        489,
        "Cyber Ireland 2022 Report",
    )

    insert_metric(
        conn,
        "firm_count",
        "Ireland",
        "dedicated",
        2021,
        160,
        "Cyber Ireland 2022 Report",
    )

    insert_metric(
        conn,
        "firm_count",
        "Ireland",
        "diversified",
        2021,
        329,
        "Cyber Ireland 2022 Report",
    )

    insert_metric(
        conn,
        "firm_count",
        "Cork",
        "total",
        2021,
        129,
        "Cyber Ireland 2022 Report",
    )

    insert_metric(
        conn,
        "firm_count",
        "Kerry",
        "total",
        2021,
        5,
        "Cyber Ireland 2022 Report",
    )

    insert_metric(
        conn,
        "firm_count",
        "South-West",
        "total",
        2021,
        134,
        "Cyber Ireland 2022 Report",
    )

    # -------------------------
    # Employment Metric (Test 1)
    # -------------------------

    insert_metric(
        conn,
        "employment",
        "Ireland",
        "workforce",
        2022,
        7351,
        "Cyber Ireland 2022 Report",
    )

    conn.commit()
    conn.close()

    print("Metrics warehouse built successfully.")


if __name__ == "__main__":
    build_metrics()