from pymongo import MongoClient
from datetime import datetime, timedelta
import json

MONGO_URI = "your-mongodb-uri"
DATABASE_NAME = "production"
COLLECTION_NAME = "transactions"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

archive_date = datetime.utcnow() - timedelta(days=7)

records = list(collection.find({
    "createdAt": {"$lt": archive_date}
}))

with open("mongodb_archive.json", "w") as archive_file:
    json.dump(records, archive_file, default=str)

print(f"Archived {len(records)} MongoDB records")
