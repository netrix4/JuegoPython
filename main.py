import cv2 as cv
from PIL import Image
import pytesseract
import re

cap = cv.VideoCapture(2)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)

    print("Camera opened successfully!")
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from camera.")
            break
        
        detected_text = pytesseract.image_to_string(frame)


        if re.search(r'\w+', detected_text) :
            print('Algun texto encontrado: ', detected_text.strip() )

        cv.imshow(mat=frame, winname='Camera Feed')
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
