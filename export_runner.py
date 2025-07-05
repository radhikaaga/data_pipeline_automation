from pymongo import MongoClient
from export_utils import export_collection

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]

collections = ["students", "teachers", "courses"]
for col in collections:
    export_collection(db, col)
