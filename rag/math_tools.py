import re
import sqlite3

DB_PATH = "database/cyber_metrics.db"


def extract_target_jobs(query: str):
    """
    Extract target job number from query.
    Example: 'reach 20000 jobs'
    """

    numbers = re.findall(r"\d{4,6}", query)

    if numbers:
        return int(numbers[0])

    return None


def get_baseline_jobs():
    """
    Retrieve baseline employment from metrics database.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT value
        FROM metrics
        WHERE metric_name='employment'
        LIMIT 1
    """)

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]

    return None


def calculate_cagr():

    start_value = 7351
    end_value = 17000
    years = 9

    cagr = (end_value / start_value) ** (1 / years) - 1

    return {
        "start_value": start_value,
        "end_value": end_value,
        "years": years,
        "cagr": round(cagr,6),
        "percentage": round(cagr * 100,2),
        "formula": "(17000/7351)^(1/9) - 1"
    }


def calculate_cagr_from_query(query: str):
    """
    Full pipeline for dynamic CAGR calculation.
    """

    start_value = get_baseline_jobs()

    if not start_value:
        raise ValueError("Baseline employment not found in database.")

    end_value = extract_target_jobs(query)

    if not end_value:
        end_value = 17000

    years = 9

    return calculate_cagr(start_value, end_value, years)