import os
import sys
import json
from datetime import datetime

def load_input_schema(folder_path):
    path = os.path.join(folder_path, "1b_input.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_parsed_sections(folder_path):
    path = os.path.join(folder_path, "parsed.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def rank_sections(parsed_data):
    ranked = []
    all_sections = []

    for doc in parsed_data:
        doc_name = doc["document"]
        for section in doc.get("sections", []):
            heading = section.get("heading", "").strip()
            page = section.get("page", -1)
            if heading and page != -1:
                all_sections.append({
                    "document": doc_name,
                    "section_title": heading,
                    "page_number": page
                })

    # Limit to top 5 (can later add better scoring)
    for idx, sec in enumerate(all_sections[:5], start=1):
        sec["importance_rank"] = idx
        ranked.append(sec)
    
    return ranked

def extract_subsections(parsed_data):
    refined = []
    for doc in parsed_data:
        doc_name = doc["document"]
        for section in doc.get("sections", []):
            refined.append({
                "document": doc_name,
                "refined_text": section.get("content", "").strip(),
                "page_number": section.get("page", -1)
            })
    return refined

def build_output(input_schema, parsed_data):
    return {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_schema["documents"]],
            "persona": input_schema["persona"]["role"],
            "job_to_be_done": input_schema["job_to_be_done"]["task"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": rank_sections(parsed_data),
        "subsection_analysis": extract_subsections(parsed_data)
    }

def save_output(output, folder_path):
    output_path = os.path.join(folder_path, "1b_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    print(f"✅ Output saved to: {output_path}")

def main(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    try:
        input_schema = load_input_schema(folder_path)
        parsed_data = load_parsed_sections(folder_path)
        result = build_output(input_schema, parsed_data)
        save_output(result, folder_path)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_relevant.py <PDF_FOLDER_PATH>")
        sys.exit(1)

    folder_path = sys.argv[1]
    main(folder_path)