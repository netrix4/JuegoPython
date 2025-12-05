import cv2 as cv
import pytesseract
import re
import tkinter as tk

roi_coordinates = [(135, 60), (540, 270)]
correct_word_count = 0
last_detected_word = ""

WORD_SET_1 = ["HOJA", "SAL"]
WORD_SET_2 = ["GATO", "MONO"]
WORD_SET_3 = ["AGUA", "HOJA"]

SELECTED_WORDS = []

def read_from_camera_image(frame):
    global correct_word_count, last_detected_word

    cv.putText(frame, 'OCR', (10, 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255))
    print('Leyendo texto en la imagen...')

    (x1, y1) = roi_coordinates[0]
    (x2, y2) = roi_coordinates[1]
    roi = frame[y1:y2, x1:x2]

    detected_text = pytesseract.image_to_string(roi).strip().upper()

    if not re.search(r'[A-Z]', detected_text):
        print("No se detectó texto útil.")
        return

    print("Texto encontrado:", detected_text)

    if detected_text in SELECTED_WORDS:

        if detected_text != last_detected_word:
            correct_word_count += 1
            print("¡Palabra correcta! Contador:", correct_word_count)

            last_detected_word = detected_text
        else:
            print("Palabra repetida, no se suma.")

    else:
        print("La palabra no pertenece al conjunto actual.")


def main():
    global correct_word_count
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 360)

    print("¡Cámara conectada!")
    print("Palabras del conjunto seleccionado:", SELECTED_WORDS)

    while True:
        ret, frame = cap.read()
        frame = cv.rotate(frame, cv.ROTATE_180)

        if correct_word_count == 2:
            cv.putText(frame, 'GANASTE!',
                       (int(roi_coordinates[0][0] + 80),
                        int(roi_coordinates[1][1] / 2) + roi_coordinates[0][1]),
                       cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (0, 255, 0))
            print('¡GANASTE!')

            cv.imshow('Aprendiendo a leer y escribir', frame)
            cv.waitKey(5000)
            break

        cv.rectangle(frame, roi_coordinates[0], roi_coordinates[1], (0, 240, 0), 2)
        cv.putText(frame, 'Coloca tus tarjetas',
                   (roi_coordinates[0][0] + 10, roi_coordinates[0][1] - 15),
                   cv.FONT_HERSHEY_COMPLEX_SMALL, 0.85, (255, 255, 255))
        cv.putText(frame, f"{correct_word_count}/2",
                   (roi_coordinates[0][0] + 10, roi_coordinates[0][1] - 27),
                   cv.FONT_HERSHEY_COMPLEX_SMALL, 0.85, (255, 255, 255))

        if not ret:
            print("Error: no se pudo leer la cámara.")
            break

        cv.imshow('Aprendiendo a leer y escribir', frame)

        pressed = cv.waitKey(1) & 0xFF
        if pressed == ord('r'):
            read_from_camera_image(frame)
        if pressed == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

def select_word_set(word_set):
    global SELECTED_WORDS
    SELECTED_WORDS = word_set
    print("Conjunto seleccionado:", word_set)
    root.destroy()
    main()

root = tk.Tk()
root.title("Selecciona un conjunto de palabras")

tk.Label(root, text="Elige el conjunto para el juego:", font=("Arial", 12)).pack(pady=10)

btn1 = tk.Button(root, text="Conjunto 1 (Hoja, Sal)", width=25,
                 command=lambda: select_word_set(WORD_SET_1))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Conjunto 2 (Gato, Mono)", width=25,
                 command=lambda: select_word_set(WORD_SET_2))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Conjunto 3 (Agua, Hoja)", width=25,
                 command=lambda: select_word_set(WORD_SET_3))
btn3.pack(pady=5)

root.mainloop()
