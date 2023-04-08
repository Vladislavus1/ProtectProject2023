import cv2
# import numpy as np

# img = cv2.imread('test_images/man.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filename = "man2.jpg"

def face_detection(filename):
    img = cv2.imread(f"images/{filename}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier('face.xml')
    min_n = 1
    results = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_n)
    print(results)
    if len(results) == 0:
        print("No outline of face or body was found")
        return "Empty"
    else:
        print(results)
        while len(results) != 1:
            min_n += 1
            results = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_n)
            if len(results) == 1:
                break
            elif len(results) == 0:
                print("There s some problems with finding a coordinates")
                return "ERROR"
        for (x, y, w, h) in results:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)
        cv2.imwrite(f"static/results.img/{filename}", img)
        print("Successfully redacted!")

def fullbody_detection(filename):
    img = cv2.imread(f"images/{filename}")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fullbody = cv2.CascadeClassifier('fullbody.xml')
    min_n = 1
    results = fullbody.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_n)
    if len(results) == 0:
        print("No outline of face or body was found")
        return "Empty"
    else:
        print(results)
        while len(results) != 1:
            min_n += 1
            results = fullbody.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=min_n)
            if len(results) == 1:
                break
            elif len(results) == 0:
                print("There s some problems with finding a coordinates")
                return "ERROR"
        for (x, y, w, h) in results:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
        cv2.imwrite(f"static/results.img/{filename}", img)
        print("Successfully redacted!")








