import os
import face_recognition
from PIL import Image


def findPerson():
    image_of_irshad = face_recognition.load_image_file('Image/irshad.jpg')
    irshad_face_encoding = face_recognition.face_encodings(image_of_irshad)[0]

    path = 'C:\\Users\\Irshad\\PycharmProjects\\Face-Recognition\\SavedImages'
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            image = face_recognition.load_image_file('SavedImages/' + file)
            image_encoding = face_recognition.face_encodings(image)
            if not len(image_encoding):
                print(image, "can't be encoded")
                continue
            # Compare faces
            results = face_recognition.compare_faces(
                [irshad_face_encoding], image_encoding[0],tolerance=0.50)

            if results[0]:
                print('Found at:' + file)
                pill = Image.fromarray(image)
                pill.show()
            else:
                print('Not Found')
