import pdfplumber
import json
import os


def extract_text_with_pages(pdf_path: str):
    """
    Extract text page-by-page from PDF.
    Returns list of dicts with page metadata.
    """
    all_pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            if text and text.strip():
                page_data = {
                    "page": i + 1,
                    "content": text.strip(),
                    "type": "narrative",
                    "source": os.path.basename(pdf_path)
                }

                all_pages.append(page_data)

    return all_pages


def save_to_json(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    PDF_PATH = "cyber_ireland_2022.pdf"
    OUTPUT_PATH = "storage/text_data.json"

    print("Extracting text from PDF...")
    pages = extract_text_with_pages(PDF_PATH)
    save_to_json(pages, OUTPUT_PATH)
    print(f"Extraction complete. Saved to {OUTPUT_PATH}")