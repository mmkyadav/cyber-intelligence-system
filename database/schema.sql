-- Raw tables metadata
CREATE TABLE IF NOT EXISTS raw_tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT,
    page_number INTEGER,
    row_count INTEGER,
    column_count INTEGER
);

-- Curated Metrics Warehouse
CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metric_name TEXT NOT NULL,
    region TEXT,
    category TEXT,
    year INTEGER,
    value REAL NOT NULL,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Regions reference table
CREATE TABLE IF NOT EXISTS regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_name TEXT UNIQUE NOT NULL,
    region_type TEXT
);