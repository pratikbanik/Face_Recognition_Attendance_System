
# Face Recognition Attendance System

The Face Recognition Attendance System is an innovative solution leveraging advanced face recognition technology to automate attendance marking. Developed using the Flask web framework and integrated with Firebase for secure database management, this system ensures precise, real-time attendance tracking.

Powered by Python libraries like OpenCV and dlib for robust face detection and recognition, alongside numpy, pandas, and matplotlib for data manipulation and visualization, it delivers dependable performance with user-friendly operation. The intuitive web interface offers distinct functionalities: student access, admin access for managing user data and attendance records, and a feature to view the attendance list.

Students can securely log in to access personal and attendance details, while admins enjoy capabilities such as adding, deleting, and clearing records. The system guarantees accurate detection and verification of faces, promptly marking attendance upon successful recognition and notifying users accordingly.

By eliminating the need for physical contact and reducing human error, this modern approach enhances efficiency compared to traditional methods, establishing the Face Recognition Attendance System as a trusted and efficient tool for attendance management.


## Technical Requirements

### Programming Language:

Python: The primary language for backend development and face recognition algorithms.

### Frameworks and Libraries:

- Flask: For building the web application and server-side logic.

- OpenCV: For real-time face detection using computer vision techniques.

- dlib: For face landmark detection and feature extraction.

- face-recognition: For comparing detected faces with stored images.

- cvzone: For additional computer vision functionalities.

- firebase_admin: For integrating with Firebase for database management.

### Database:

Firebase: Used for storing user data, attendance records, and handling authentication.

### Web Technologies:

- HTML: For structuring the web pages.

- CSS: For styling the web pages and improving the user interface.

### Hardware:

- A computer with a webcam for capturing live video feed.

- Sufficient processing power to handle real-time face detection and recognition.

### Software:

- Python environment set up with all required libraries installed.

- Firebase account set up and configured for the application.

### Dependencies:

- numpy
- pandas
- matplotlib
- seaborn
- opencv-python
- cmake
- dlib
- face-recognition
- cvzone
- firebase_admin
- flask


## Features

- Face Detection and Recognition
- User Roles and Access
- Attendance Management
- Web Interface
- Security and Privacy


## Deployment

### Clone the Repository:

Use Git to clone the repository to your local machine:

```bash
git clone https://github.com/pratikbanik/Face_Recognition_Attendance_System.git
```

```bash
cd Face_Recognition_Attendance_System
```


## Environment Setup

To ensure that the deployment environment is correctly set up, follow these guidelines:

- Ensure that Python 3.7 or higher is installed on your machine. You can download the latest version of Python from the official Python website.

- Ensure that C++ is installed on your machine. You can download it from Microsoft Visual Studio (Desktop Development with C++).

- Use a virtual environment to manage dependencies. Create and activate a virtual environment using the following commands:

```bash
python -m venv venv
```

```bash
venv\Scripts\activate (Windows)
```


## Install Required Libraries:

Install all the necessary Python libraries using pip. This can be done by installing the libraries listed in the “requirements.txt” file.

```bash
pip install -r requirements.txt
```


## Set Up Firebase:

- Create a Firebase project if you don't have one.
- Set up a Firebase Realtime Database.
- Set up a Firebase Storage Bucket.
- Generate a Firebase Admin SDK private key from the Firebase console and save it as serviceAccountKey.json in your project directory.
- Update the Firebase configuration in the code to match your Firebase project's settings.


## Run the Web Application:

### Activate the Virtual Environment (venv) :

```bash
cd main
```

```bash
python database.py
```

```bash
python encoder.py
```

```bash
python app.py
```

### Start the Flask server

```bash
python webapp.py
```


## Screenshots

![attendance-count](https://github.com/pratikbanik/Face_Recognition_Attendance_System/assets/104691152/cb389a66-e6f7-4ca7-b66f-5acd1da6c611)

![Dashboard](https://github.com/pratikbanik/Face_Recognition_Attendance_System/assets/104691152/5f15fca4-327e-46e1-ac42-a51d3c8e2522)

![Profile](https://github.com/pratikbanik/Face_Recognition_Attendance_System/assets/104691152/88cf176a-bf96-470f-b046-e8852681cdb9)

![AttendanceList](https://github.com/pratikbanik/Face_Recognition_Attendance_System/assets/104691152/08b70e7c-8c51-4127-abb0-a9e4631a733f)


## Acknowledgements

 - [Face Recognition Library](https://github.com/ageitgey/face_recognition)
 - [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)
 - [Firebase Documentation](https://firebase.google.com/docs)
 - [OpenCV Documentation](https://docs.opencv.org/4.x/)
 - [Dlib Documentation](http://dlib.net/)
 - [Python Official Documentation](https://docs.python.org/3/)
