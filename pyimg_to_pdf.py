from PIL import Image
from tkinter import Tk, filedialog

def image_to_pdf(image_path, pdf_path):
    # Open the image file
    image = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not already in that mode
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    # Save the image as a PDF
    image.save(pdf_path, 'PDF', resolution=100.0)

# Function to open a file dialog and convert the selected image to PDF
def select_image_and_convert():
    # Create a Tkinter root window (it won't be shown)
    root = Tk()
    root.withdraw()  # Hide the root window
    
    # Open a file dialog to select an image file
    image_path = filedialog.askopenfilename(title='Select an image file', filetypes=[('Image files', '*.jpg *.jpeg *.png *.bmp *.gif')])
    
    if image_path:
        # Define the output PDF path
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[('PDF files', '*.pdf')], title="Save PDF as")
        
        if pdf_path:
            # Convert the image to PDF
            image_to_pdf(image_path, pdf_path)
            print(f"Image converted to PDF and saved as {pdf_path}")
        else:
            print("No PDF file path provided.")
    else:
        print("No image file selected.")

# Run the function to select an image and convert it to PDF
select_image_and_convert()
