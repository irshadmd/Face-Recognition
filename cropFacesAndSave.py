import cv2
import datetime


def cropFacesAndSave():
    face_Cascade = cv2.CascadeClassifier("HaarCascade/haarcascade_frontalface_default.xml")

    capture = cv2.VideoCapture(0)
    count = 0

    while capture:
        flag, frame = capture.read()
        if flag:

            year = str(datetime.datetime.now().year)
            month = str(datetime.datetime.now().month)
            day = str(datetime.datetime.now().day)
            hr = str(datetime.datetime.now().hour)
            min = str(datetime.datetime.now().minute)
            sec = str(datetime.datetime.now().second)
            dateTime = day + '-' + month + '-' + year + '_' + hr + '-' + min + '-' + sec

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_Cascade.detectMultiScale(gray_img, 1.1, 6)

            for (x, y, w, h) in faces:
                count += 1
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3, cv2.LINE_AA)
                croped_face = frame[y:y + h, x:x + w]
                FILE_NAME = 'SavedImages\IMG_' + dateTime + '_' + str(count) + '.jpg'
                cv2.imwrite(FILE_NAME, croped_face)

            cv2.imshow("Capturing", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    capture.release()
    cv2.destroyAllWindows()


