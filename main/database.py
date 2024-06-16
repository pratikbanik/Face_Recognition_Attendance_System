# Import Dependencies

import firebase_admin                         # For Firebase integration
from firebase_admin import credentials        # For Firebase credentials
from firebase_admin import db                 # For Firebase Realtime Database


# Firebase Authentication
cred = credentials.Certificate("Your Key")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "Your URL"
    }
)


# Reference to the "Students" directory in the database
ref = db.reference("Students")


# Sample student data
data = {
    "33401221032":      # id of student which is a key
    {
        "id": "33401221032",
        "name": "Pratik Banik",
        "password": "123",
        "dob": "01-01-2001",
        "address": "College-Para, Siliguri",
        "phone": "0123456789",
        "email": "pratik@gmail.com",
        "major": "BCA",
        "starting_year": 2021,
        "standing": "G",
        "total_attendance": 10,
        "year": "3rd",
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    }
}


# Add student data to the database
for key, value in data.items():
    ref.child(key).set(value)