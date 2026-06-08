import sqlite3

conn = sqlite3.connect(
    "bankissue.db"
)

cursor = conn.cursor()

print("\n========== FINDINGS TABLE ==========\n")

cursor.execute(
    "SELECT * FROM findings"
)

for row in cursor.fetchall():

    print(row)

print("\n========== REPORTS TABLE ==========\n")

cursor.execute(
    "SELECT * FROM reports"
)

for row in cursor.fetchall():

    print(row)

conn.close()