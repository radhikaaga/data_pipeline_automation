from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]

# Create collection and insert dummy data
students = db["students"]
students.insert_many([
    {"id": 1, "name": "Aarav Sharma", "age": 20, "department": "CSE"},
    {"id": 2, "name": "Priya Mehta", "age": 21, "department": "IT"}
])

print("Student DB created with data.")
