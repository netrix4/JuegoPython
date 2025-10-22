import pytesseract
from PIL import Image

# Open an image file
img = Image.open('./superC.png')

# Use pytesseract to extract text
text = pytesseract.image_to_string(img)
print(text)


# import easyocr
# from PIL import Image

# # Initialize the OCR reader (specify languages)
# reader = easyocr.Reader(['en'])

# # Read text from an image
# results = reader.readtext('./superC.png')

# for (bbox, text, prob) in results:
#     print(f"Detected text: {text}, Confidence: {prob:.2f}")
#     # print(f"Detected text: {text}")


# img = Image.open('./superC.png')
# img.show('title')