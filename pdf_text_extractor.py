from pdfminer.high_level import extract_text


def extract(pdf_path):
    """Extracts text from a PDF file and creates a new txt file in raws with the same name as the PDF file."""
    text = extract_text(pdf_path)
    pdf_name = pdf_path.split("/")[-1]
    pdf_name_without_extension = pdf_name.split(".")[0]
    txt_path = f"raws/{pdf_name_without_extension}.txt"
    with open(txt_path, "w") as f:
        f.write(text)
    return txt_path


extract("textbooks/stanford_ml_notes.pdf")
