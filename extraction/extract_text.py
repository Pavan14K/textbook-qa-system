import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    
    text = extract_text_from_pdf(pdf_path)
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(text)