import sqlite3


def initialize_database():

    conn = sqlite3.connect(
        "bankissue.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS findings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        category TEXT,

        finding TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        report_text TEXT
    )
    """)

    conn.commit()

    conn.close()


def save_findings(findings):

    conn = sqlite3.connect(
        "bankissue.db"
    )

    cursor = conn.cursor()

    for category, items in findings.items():

        for item in items:

            cursor.execute(
                """
                INSERT INTO findings
                (category, finding)

                VALUES (?, ?)
                """,
                (
                    category,
                    item
                )
            )

    conn.commit()

    conn.close()


def save_report(report_text):

    conn = sqlite3.connect(
        "bankissue.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reports
        (report_text)

        VALUES (?)
        """,
        (
            report_text,
        )
    )

    conn.commit()

    conn.close()