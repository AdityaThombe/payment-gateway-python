"""Order storage in SQLite."""
import sqlite3


def connect(path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, merchant TEXT, customer TEXT, amount INTEGER)"
    )
    return conn


def add_order(conn: sqlite3.Connection, merchant: str, customer: str, amount: int) -> int:
    cur = conn.execute(
        "INSERT INTO orders (merchant, customer, amount) VALUES (?, ?, ?)", (merchant, customer, amount)
    )
    conn.commit()
    return cur.lastrowid


def search_orders(conn: sqlite3.Connection, merchant: str, customer: str) -> list:
    """Orders of one merchant for a customer name typed into the dashboard search box."""
    query = f"SELECT id, customer, amount FROM orders WHERE merchant = '{merchant}' AND customer = '{customer}'"
    return conn.execute(query).fetchall()


def total_for(conn: sqlite3.Connection, merchant: str) -> int:
    row = conn.execute("SELECT COALESCE(SUM(amount), 0) FROM orders WHERE merchant = ?", (merchant,)).fetchone()
    return row[0]
