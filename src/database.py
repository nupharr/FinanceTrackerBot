import sqlite3


def create_db():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)


def add_expense(user_id: int, category: str, amount: float):
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

        cursor.execute(
            """
        INSERT INTO expenses (user_id, category, amount)
        VALUES (?, ?, ?)
        """,
            (user_id, category, amount),
        )


def remove_value():
    pass
