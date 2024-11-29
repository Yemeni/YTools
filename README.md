# Utility Tools for OCR, PDF, and Image Processing

This repository contains four utility tools for OCR, PDF splitting/merging, and image-to-PDF conversion. Each tool is designed to make common tasks simple and efficient.

---

## Tools Overview

### 1. **OCR from Clipboard**
A script to extract text from an image copied to the clipboard using Tesseract OCR.

### 2. **Split PDF with Page Numbers**
A script to split a PDF into separate pages, save non-empty pages as individual PDFs, and optionally delete the original file.

### 3. **Image to PDF Converter**
A script to convert image files (e.g., JPG, PNG) to a PDF.

### 4. **Merge PDFs with Custom Page Order**
A script to merge multiple PDF files into a single PDF with a user-defined page order.

---

## How to Use the Tools

### 1. **OCR from Clipboard**
Extracts text from an image copied to the clipboard and copies the recognized text back to the clipboard.

#### Requirements:
- Install Tesseract OCR.
- Install required Python libraries:
```bash
pip install pytesseract pyperclip pillow
```

#### Usage:
1. Copy an image to your clipboard.
2. Run the script:
```bash
python ocr_from_clipboard.py
```
3. The extracted text will be printed and copied to your clipboard.

---

### 2. **Split PDF with Page Numbers**
Splits a PDF into individual pages, skipping empty pages.

#### Requirements:
- Install required Python libraries:
```bash
pip install PyPDF2
```

#### Usage:
1. Run the script:
```bash
python split_pdf_with_numbers.py
```
2. Select a PDF file via the file dialog.
3. Non-empty pages will be saved as individual PDFs in the same directory.
4. Optionally, you can delete the original file after splitting.

---

### 3. **Image to PDF Converter**
Converts an image file into a PDF file.

#### Requirements:
- Install required Python libraries:
```bash
pip install pillow
```

#### Usage:
1. Run the script:
```bash
python image_to_pdf_converter.py
```
2. Select an image file via the file dialog.
3. Choose a location and filename to save the resulting PDF.
4. The PDF will be created and saved.

---

### 4. **Merge PDFs with Custom Page Order**
Merges multiple PDF files into a single PDF in a user-defined page order.

#### Requirements:
- Install required Python libraries:
```bash
pip install PyPDF2
```

#### Usage:
1. Run the script:
```bash
python merge_pdfs_with_order.py
```
2. Select multiple PDF files via the file dialog.
3. Enter the desired page order (e.g., `1 2 3 1 2`).
4. Choose a location and filename to save the merged PDF.
5. The merged PDF will be created and saved.

---

## Notes
- Ensure Python 3.6+ is installed on your system.
- For OCR functionality, download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

---

## License
This repository is licensed under the MIT License. See `LICENSE` for more information.
