import sqlite3

DB_PATH = "database/cyber_sector.db"

def analyze_region(query: str):

    query_lower = query.lower()

    region = None

    if "cork" in query_lower:
        region = "Cork"

    elif "kerry" in query_lower:
        region = "Kerry"

    elif "south-west" in query_lower or "southwest" in query_lower:
        region = "South-West"

    if region is None:
        return {"error": "Region not detected"}

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT value FROM metrics
        WHERE metric_name='firm_count'
        AND region=?
        AND category='total'
    """, (region,))

    regional = cursor.fetchone()

    cursor.execute("""
        SELECT value FROM metrics
        WHERE metric_name='firm_count'
        AND region='Ireland'
        AND category='total'
    """)

    national = cursor.fetchone()

    conn.close()

    if not regional or not national:
        return {"error": "Data not found"}

    regional_value = regional[0]
    national_value = national[0]

    share = regional_value / national_value

    return {
        "region": region,
        "regional_firms": regional_value,
        "national_total": national_value,
        "regional_share": round(share,4),
        "percentage": round(share*100,2)
    }