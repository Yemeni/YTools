import pytesseract
import pyperclip
from PIL import ImageGrab

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your tesseract.exe path

def ocr_from_clipboard():
    # Capture the image from the clipboard
    img = ImageGrab.grabclipboard()
    
    if isinstance(img, ImageGrab.Image.Image):
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        
        # Copy the recognized text to the clipboard
        pyperclip.copy(text)
        
        print("Text copied to clipboard:")
        print(text)
    else:
        print("No image found in clipboard!")

# Run the OCR function
ocr_from_clipboard()
