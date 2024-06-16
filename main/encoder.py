# Import Dependencies

import cv2                         # For image processing
import pickle                      # For serialization
import face_recognition            # For face recognition
import os                          # For interacting with the operating system

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


# Student images directory
folderPath = "static/Files/Images"
imgPathList = os.listdir(folderPath)
print(imgPathList)
imgList = []
studentIDs = []


# Loop through the images in the directory
for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))# Read image
    studentIDs.append(os.path.splitext(path)[0])# Extract student ID from file name

    # Upload image to Firebase storage
    fileName = f"{folderPath}/{path}"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIDs)

def findEncodings(images):
    encodeList = []

    # Encode faces in the images
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started")


# Find encodings for the images
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIDs]


print("Encoding Ended")


# Save the encodings to a pickle file
file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")