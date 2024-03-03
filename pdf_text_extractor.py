from pdfminer.high_level import extract_text
from pathlib import Path
import os


def extract(pdf_path):
    """Extracts text from a PDF file and creates a new txt file in raws with the same name as the PDF file."""
    text = extract_text(pdf_path)
    pdf_path = Path(pdf_path)
    txt_path = Path("raws") / f"{pdf_path.stem}.txt"
    with txt_path.open("w") as f:
        f.write(text)
    return str(txt_path)


dest = os.path.join("textbooks", "ISLP_website.pdf")
extract(dest)
