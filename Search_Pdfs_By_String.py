
# seraching pdf for specific strings

import os
import fitz  # PyMuPDF

def search_pdfs(folder_path, search_string):
    matching_files = []

    # Walk through all files and subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                try:
                    with fitz.open(pdf_path) as pdf_doc:
                        for page in pdf_doc:
                            if search_string.lower() in page.get_text().lower():
                                matching_files.append(pdf_path)
                                break  # No need to check further pages if a match is found
                except Exception as e:
                    print(f"Error reading {pdf_path}: {e}")

    return matching_files

# Example usage
folder_to_search = input("Enter folder path to search for PDFs: ")
string_to_search = input("Enter the string to search within PDFs: ")

results = search_pdfs(folder_to_search, string_to_search)

if results:
    print("\nMatching PDF files:")
    for pdf in results:
        print(pdf)
else:
    print("No matching PDFs found.")
