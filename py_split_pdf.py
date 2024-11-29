import os
from tkinter import Tk, filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_with_numbers():
    # Hide the root Tkinter window
    Tk().withdraw()

    # Open file dialog to select a PDF file
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        print("No file selected.")
        return

    # Get the directory and filename of the selected PDF
    directory = os.path.dirname(file_path)
    base_filename = os.path.splitext(os.path.basename(file_path))[0]

    try:
        # Read the selected PDF file
        pdf_reader = PdfReader(file_path)
        empty_pages_skipped = 0
        
        for i, page in enumerate(pdf_reader.pages):
            # Check if the page has content
            if page.extract_text().strip():  # Only save non-empty pages
                pdf_writer = PdfWriter()
                pdf_writer.add_page(page)
                
                # Save each non-empty page as a new PDF file
                output_file = os.path.join(directory, f"{base_filename}_P_{i + 1 - empty_pages_skipped}.pdf")
                with open(output_file, "wb") as output_pdf:
                    pdf_writer.write(output_pdf)
            else:
                empty_pages_skipped += 1  # Increment the count of skipped pages

        print(f"PDF split successfully! Empty pages skipped: {empty_pages_skipped}")

        # Ask if the user wants to delete the original file
        delete_original = messagebox.askyesno("Delete Original File", "Do you want to delete the original file?")
        if delete_original:
            os.remove(file_path)
            print(f"Original file '{os.path.basename(file_path)}' deleted.")

    except Exception as e:
        print(f"Error splitting PDF: {e}")

if __name__ == "__main__":
    split_pdf_with_numbers()
