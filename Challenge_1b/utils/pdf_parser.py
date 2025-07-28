import os
import fitz  
import json
from tqdm import tqdm
from datetime import datetime

def is_heading(line):
    # Detect H1 or H2 based on capitalization and length heuristics
    if line.isupper() and len(line.split()) <= 10 and len(line) > 5:
        return "H1"
    if line.istitle() and len(line.split()) <= 12:
        return "H2"
    return None


def parse_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        for b in blocks:
            text = b[4].strip()
            if len(text) == 0:
                continue

            heading_level = is_heading(text)
            if heading_level:
                sections.append({
                    "heading": text,
                    "level": heading_level,
                    "page": page_num,
                    "content": ""  # optionally, collect following lines
                })

    return sections


def main(pdf_folder_path):
    output = []

    for file in tqdm(os.listdir(pdf_folder_path)):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_folder_path, file)
            parsed = parse_pdf(path)
            output.append({
                "document": file,
                "sections": parsed
            })

    output_dir = os.path.join("Inputs")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "parsed.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Parsing complete. Output saved to {output_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python pdf_parser.py <PDF_FOLDER_PATH>")
    else:
        main(sys.argv[1])
