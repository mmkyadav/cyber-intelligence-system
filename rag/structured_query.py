import sqlite3

DB_PATH = "database/cyber_sector.db"


def compare_pureplay_concentration():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Total firms nationally
    cursor.execute("""
        SELECT value FROM metrics
        WHERE metric_name='firm_count'
        AND region='Ireland'
        AND category='total'
    """)
    national_total = cursor.fetchone()[0]

    # Dedicated (Pure-play) firms nationally
    cursor.execute("""
        SELECT value FROM metrics
        WHERE metric_name='firm_count'
        AND region='Ireland'
        AND category='dedicated'
    """)
    national_dedicated = cursor.fetchone()[0]

    # South-West total firms
    cursor.execute("""
        SELECT value FROM metrics
        WHERE metric_name='firm_count'
        AND region='South-West'
        AND category='total'
    """)
    southwest_total = cursor.fetchone()[0]

    conn.close()

    # Calculate concentrations
    national_concentration = national_dedicated / national_total
    southwest_share = southwest_total / national_total

    return {
        "national_pureplay_concentration": national_concentration,
        "southwest_share_of_total_firms": southwest_share,
        "note": "Regional dedicated breakdown not provided in report; comparison based on total firm distribution."
    }


if __name__ == "__main__":

    result = compare_pureplay_concentration()

    print(result)