from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]

# Add teachers
db["teachers"].insert_many([
    {"id": 101, "name": "Dr. Rakesh", "subject": "Compiler Design"},
    {"id": 102, "name": "Ms. Isha", "subject": "AI"}
])

# Add courses
db["courses"].insert_many([
    {"course_id": "CS101", "title": "Data Structures", "credits": 3},
    {"course_id": "CS102", "title": "Machine Learning", "credits": 4}
])

print("Sample data added to teachers and courses.")
