import schedule
import time
from pymongo import MongoClient
from export_utils import export_collection

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]

def job():
    collections = ["students", "teachers", "courses"]
    for col in collections:
        export_collection(db, col)

# Run every day at 1:00 AM
schedule.every().day.at("01:00").do(job)


print("🕒 Scheduler running. Waiting for scheduled time...")
while True:
    schedule.run_pending()
    time.sleep(1)
