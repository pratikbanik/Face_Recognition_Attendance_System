# Import Dependencies

import cv2                         # For image processing
import os                          # For interacting with the operating system
import pickle                      # For serialization
import face_recognition            # For face recognition
import numpy as np                 # For numerical operations
import cvzone                      # For additional computer vision utilities
from datetime import datetime      # For handling date and time

import firebase_admin                         # For Firebase integration
from firebase_admin import credentials        # For Firebase credentials
from firebase_admin import db                 # For Firebase Realtime Database
from firebase_admin import storage            # For Firebase Storage


# Firebase authentication
cred = credentials.Certificate("Your Key")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "Your URL",
        "storageBucket": "Your Bucket"
    }
)


bucket = storage.bucket()       # Accessing Firebase storage bucket


# Accessing the webcam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # width .... CAP_PROP_FRAME_WIDTH ---> 3
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # height .... CAP_PROP_FRAME_HEIGHT ---> 4


# Loading background image
imgBackground = cv2.imread("static/Files/Resources/background.png")


# Loading mode images
folderModePath = "static/Files/Resources/Modes/"
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))


# Loading face encodings from pickle file 
# ---> to identify if the person is in our database or not.... to detect faces that are known or not
file = open("EncodeFile.p", "rb")
encodeListKnownWithIds = pickle.load(file)
file.close()
encodedFaceKnown, studentIds = encodeListKnownWithIds
# print(studentIds)


# Initializing variables
modeType = 0
id = -1
imgStudent = []
counter = 0


# Main loop for processing webcam feed
while True:
    success, img = capture.read()

    # Resize and convert image to RGB for face recognition
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    # Detect faces in the current frame
    faceCurrentFrame = face_recognition.face_locations(imgSmall)
    encodeCurrentFrame = face_recognition.face_encodings(imgSmall, faceCurrentFrame)

    # Overlay webcam feed on background image
    imgBackground[162 : 162 + 480, 55 : 55 + 640] = img
    imgBackground[44 : 44 + 633, 808 : 808 + 414] = imgModeList[modeType]

    if faceCurrentFrame:  
        for encodeFace, faceLocation in zip(encodeCurrentFrame, faceCurrentFrame):
            matches = face_recognition.compare_faces(encodedFaceKnown, encodeFace)
            faceDistance = face_recognition.face_distance(encodedFaceKnown, encodeFace)

            matchIndex = np.argmin(faceDistance)

            # Extract face location
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1

            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

            if matches[matchIndex] == True:
                id = studentIds[matchIndex]
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Face Detected", (65, 200), thickness=2)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

            else: 
                cvzone.putTextRect(imgBackground, "Face Detected", (65, 200), thickness=2)
                cv2.waitKey(3)
                cvzone.putTextRect(imgBackground, "Face Not Found", (65, 200), thickness=2)
                modeType = 4
                counter = 0
                imgBackground[44 : 44 + 633, 808 : 808 + 414] = imgModeList[modeType]

        if counter != 0:
            if counter == 1:
                studentInfo = db.reference(f"Students/{id}").get()

                # Get the image from the storage
                blob = bucket.get_blob(f"static/Files/Images/{id}.jpg")
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                # Update data & time of attendance
                datetimeObject = datetime.strptime(studentInfo["last_attendance_time"], "%Y-%m-%d %H:%M:%S")
                secondElapsed = (datetime.now() - datetimeObject).total_seconds()

                if secondElapsed > 30:
                    ref = db.reference(f"Students/{id}")
                    studentInfo["total_attendance"] += 1
                    ref.child("total_attendance").set(studentInfo["total_attendance"])
                    ref.child("last_attendance_time").set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44 : 44 + 633, 808 : 808 + 414] = imgModeList[modeType]

            if modeType != 3:
                if 10 < counter <= 20:
                    modeType = 2

                imgBackground[44 : 44 + 633, 808 : 808 + 414] = imgModeList[modeType]

                if counter <= 10:
                    # Render student info on background
                    # (e.g., total attendance, major, ID, standing, year, name, image)
                    # Adjust text positions based on your UI layout
                    cv2.putText(
                        imgBackground,
                        str(studentInfo["total_attendance"]),
                        (861, 125),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        1,
                    )
                    cv2.putText(
                        imgBackground,
                        str(studentInfo["major"]),
                        (1006, 550),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (255, 255, 255),
                        1,
                    )
                    cv2.putText(
                        imgBackground,
                        str(id),
                        (1006, 493),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.5,
                        (255, 255, 255),
                        1,
                    )
                    cv2.putText(
                        imgBackground,
                        str(studentInfo["standing"]),
                        (910, 625),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.6,
                        (100, 100, 100),
                        1,
                    )
                    cv2.putText(
                        imgBackground,
                        str(studentInfo["year"]),
                        (1025, 625),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.6,
                        (100, 100, 100),
                        1,
                    )
                    cv2.putText(
                        imgBackground,
                        str(studentInfo["starting_year"]),
                        (1125, 625),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.6,
                        (100, 100, 100),
                        1,
                    )

                    (w, h), _ = cv2.getTextSize(
                        str(studentInfo["name"]), cv2.FONT_HERSHEY_COMPLEX, 1, 1
                    )

                    offset = (414 - w) // 2
                    cv2.putText(
                        imgBackground,
                        str(studentInfo["name"]),
                        (808 + offset, 445),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (50, 50, 50),
                        1,
                    )

                    # Resize and Display the student image
                    imgStudentResize = cv2.resize(imgStudent, (216, 216))
                    imgBackground[175 : 175 + 216, 909 : 909 + 216] = imgStudentResize

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44 : 44 + 633, 808 : 808 + 414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break