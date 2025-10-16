import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully!")
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from camera.")
            break

        cv.imshow(mat=frame, winname='Camera Feed')
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

# import cv2
# import pytesseract
# from PIL import Image
# # Path to the Tesseract executable (replace with your path)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # Load an image containing text
# text_image_path = 'path/to/your/text_image.jpg'
# text_image = cv2.imread(text_image_path)
# # Convert the image to grayscale
# gray_text_image = cv2.cvtColor(text_image, cv2.COLOR_BGR2GRAY)
# # Use thresholding to emphasize the text
# _, thresholded_text = cv2.threshold(gray_text_image, 150, 255, cv2.THRESH_BINARY)
# # Use pytesseract to perform OCR on the thresholded image
# text = pytesseract.image_to_string(Image.fromarray(thresholded_text))
# # Display the original image and extracted text
# plt.figure(figsize=(8, 6))
# plt.imshow(cv2.cvtColor(text_image, cv2.COLOR_BGR2RGB))
# plt.title('Original Image')
# plt.axis('off')
# plt.show()
# print("Extracted Text:")
# print(text)