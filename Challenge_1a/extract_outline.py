import fitz
import os
import json
from collections import defaultdict

INPUT_DIR = "C:/Users/suhas/OneDrive/Desktop/Internships/Adobe/Challenge_1a/Inputs"
OUTPUT_DIR = "C:/Users/suhas/OneDrive/Desktop/Internships/Adobe/Challenge_1a/Outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_outline_from_pdf(filepath):
    doc = fitz.open(filepath)
    all_spans = []
    font_sizes = set()

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b["type"] != 0:
                continue
            for line in b["lines"]:
                line_text = ""
                max_font = 0
                is_bold = False
                y_coord = int(line["bbox"][1])

                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue

                    font_sizes.add(span["size"])
                    line_text += text + " "

                    if "bold" in span["font"].lower():
                        is_bold = True
                    max_font = max(max_font, span["size"])

                if line_text.strip():
                    all_spans.append({
                        "text": line_text.strip(),
                        "size": max_font,
                        "bold": is_bold,
                        "page": page_num + 1,
                        "y": y_coord
                    })

    # Heuristically determine top 3 font sizes
    sorted_sizes = sorted(list(font_sizes), reverse=True)
    size_to_level = {}
    if len(sorted_sizes) >= 1:
        size_to_level[sorted_sizes[0]] = "H1"
    if len(sorted_sizes) >= 2:
        size_to_level[sorted_sizes[1]] = "H2"
    if len(sorted_sizes) >= 3:
        size_to_level[sorted_sizes[2]] = "H3"

    outline = []
    title = None

    for item in all_spans:
        size = item["size"]
        text = item["text"]
        page = item["page"]
        bold = item["bold"]

        # Use first large, bold heading on page 1 as title
        if not title and page == 1 and size == sorted_sizes[0] and bold:
            title = text

        if size in size_to_level:
            level = size_to_level[size]
            if len(text) <= 100:  # Avoid catching large paragraphs
                outline.append({
                    "level": level,
                    "text": text,
                    "page": page
                })

    return {
        "title": title or "Untitled Document",
        "outline": outline
    }


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

    for file in sorted(pdf_files):
        file_path = os.path.join(INPUT_DIR, file)
        print(f"📄 Processing: {file}")

        try:
            output_json = extract_outline_from_pdf(file_path)
            output_name = os.path.splitext(file)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_name)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=2)

            print(f"✅ Saved outline JSON: {output_path}")
        except Exception as e:
            print(f"❌ Failed to process {file}: {str(e)}")