import cv2
import pickle
from time import sleep

def captureFaces():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier("FaceRecognitionFiles/haarcascade_frontalface_default.xml")

    # Initialize the camera
    cap = cv2.VideoCapture(0)
    count = 0
    while (count<50):
        count+=1
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]

             # Draw a rectangle around the detected face   
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Save the image if a face is detected
            if len(faces) > 0:
                for i in range(10):
                    cv2.imwrite(f"faces/me/face_detected{i}.jpg", frame)

        # Display the output
        cv2.imshow('frame', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()
    print("Faces Captured")

def recognizeFaces():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier("FaceRecognitionFiles/haarcascade_frontalface_default.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("FaceRecognitionFiles/trainner.yml")

    labels = {"person_name": 1}
    with open("FaceRecognitionFiles/labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    r = False
    confSum = 0
    count = 0
    mo = 0
    while (confSum < 1000):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            
             # Draw a rectangle around the detected face   
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Recognizer
            id_, conf = recognizer.predict(roi_gray)
            confSum+=conf
            count+=1
            if(conf>=80):
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.putText(frame, (str)(round(conf))+"%", (x+w,y), font, 1, color, stroke, cv2.LINE_AA)

        # Display the output
        cv2.imshow('frame', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()
    mo = confSum/count
    if(round(mo)>=80):
        r = True
    else:
        r = False

    return r

if __name__ == '__main__':
    captureFaces()
    #print(recognizeFaces())
