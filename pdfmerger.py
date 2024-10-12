import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    """Merge multiple PDFs into a single PDF."""
    merger = PdfMerger()

    try:
        # Append all PDFs in the list
        for pdf in pdf_list:
            print(f"Merging {pdf}...")
            merger.append(pdf)

        # Write to the output PDF file
        with open(output_filename, 'wb') as output_pdf:
            merger.write(output_pdf)

        print(f"PDFs merged successfully into {output_filename}")

    except Exception as e:
        print(f"Error during merging: {e}")

    finally:
        merger.close()

def get_pdf_files(directory):
    """Fetch all PDF files from a given directory."""
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in the directory.")
    return pdf_files

def main():
    # Specify the folder containing PDF files or files to merge
    folder_path = input("Enter the folder path where your PDFs are located: ")
    
    # Optional: You can hardcode the folder path for simplicity.
    # folder_path = "./pdfs"

    if not os.path.exists(folder_path):
        print(f"Directory {folder_path} does not exist!")
        return

    # Fetch PDF files from the folder
    pdf_files = get_pdf_files(folder_path)
    if not pdf_files:
        return

    # Specify the output PDF file name
    output_file = input("Enter the name of the output PDF file (e.g., merged.pdf): ")

    # Merge PDFs
    merge_pdfs([os.path.join(folder_path, pdf) for pdf in pdf_files], output_file)

if __name__ == "__main__":
    main()
