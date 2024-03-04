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


<<<<<<< HEAD
dest = os.path.join("textbooks", "reinforcement_learning.pdf")
extract(dest)
=======
dest = os.path.join("textbooks", "nlp.pdf")
extract(dest)
>>>>>>> 8a5606603468172b6566e3558c80ea04159807b9
