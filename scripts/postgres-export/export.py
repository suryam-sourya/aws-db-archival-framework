import psycopg2
import csv
from datetime import datetime, timedelta

connection = psycopg2.connect(
    host="your-rds-endpoint",
    database="production",
    user="postgres",
    password="password"
)

cursor = connection.cursor()
archive_date = datetime.utcnow() - timedelta(days=7)

query = "SELECT * FROM transactions WHERE created_at < %s"
cursor.execute(query, (archive_date,))

records = cursor.fetchall()

with open("postgres_archive.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(records)

print(f"Archived {len(records)} PostgreSQL records")
