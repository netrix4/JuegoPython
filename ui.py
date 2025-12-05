import cv2 as cv
import pytesseract
import re

roi_coordenates = [(135, 60), (540,270)]

def read_from_camera_image (frame):
    cv.putText(frame,'OCR',(10,10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,(255,255,255))
    print('Leyendo texto en la imagen...')

    (x1, y1) = roi_coordenates[0]
    (x2, y2) = roi_coordenates[1]
    roi = frame[y1:y2, x1:x2]

    detected_text = pytesseract.image_to_string(roi).strip()

    if re.search(r'\w+', detected_text) :
        print('Texto encontrado: ', detected_text.strip() )
        # return 
    else:
        print('No hay texto econtrado')

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
    else:
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)

        print("Camera opened successfully!")
        while True:
            ret, frame = cap.read()
            frame = cv.rotate(frame, cv.ROTATE_180)
            
            cv.rectangle(frame, roi_coordenates[0], roi_coordenates[1], (0,240,0), 2)
            cv.putText(frame,'Coloca tus tarjetas',(roi_coordenates[0][0]+10, roi_coordenates[0][1]-15), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.85,(255,255,255))

            if not ret:
                print("Error: Could not read frame from camera.")
                break

            cv.imshow(mat=frame, winname='Vision de camara')

            pressed = cv.waitKey(1) & 0xFF
            if pressed == ord('r'):
                read_from_camera_image(frame)

            if pressed == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    main()
