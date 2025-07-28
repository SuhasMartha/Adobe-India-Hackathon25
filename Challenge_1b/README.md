# 🤖 Adobe India Hackathon 2025 – Round 1B  
### **Persona-Driven Document Intelligence**  
**Theme:** *Connect What Matters — For the User Who Matters*

---

## 🚀 Overview
This repository contains our solution for **Round 1B of the Adobe India Hackathon 2025**.  
The challenge focuses on building an **intelligent document analyst** that extracts and prioritizes the most **relevant sections from a collection of documents**, tailored for a specific **persona** and their **job-to-be-done**.

---

## 🧠 Problem Statement
Given:
- A **collection of related PDF documents** (3–10 files)
- A **persona** (e.g., Travel Planner, Investment Analyst, Researcher)
- A **job-to-be-done** (task the persona wants to accomplish)

The system must:
1. Parse and analyze all input PDFs  
2. Identify and rank the most relevant sections for the persona  
3. Provide a **subsection analysis** with refined text snippets  
4. Output a **structured JSON** including:
   - Metadata  
   - Extracted sections  
   - Subsection analysis  

---

## 📂 Project Structure
```
Challenge_1b/
│── Inputs/
│ ├── Collection 1/
│ │ ├── 1b_input.json # Input schema (documents, persona, job)
│ │ ├── South of France*.pdf
│── Outputs/
│ ├── Collection 1/
│ │ ├── parsed.json # Parsed sections
│ │ ├── 1b_output.json # Final output
│── utils/
│ ├── pdf_parser.py # Extracts headings and sections
│ ├── extract_relevant.py # Ranks and refines sections
│── Dockerfile # Docker image for deployment
│── README.md # Project documentation
```

---

## ⚙️ Features
✅ Parses multiple PDFs (3–10)  
✅ Persona-aware section ranking  
✅ Refines extracted text for each subsection  
✅ Structured JSON output with metadata  
✅ CPU-only, lightweight (< 1GB model size)  
✅ Processes 3–5 documents in ≤ 60 seconds  

---

## 🔑 Input & Output

### **Input (JSON schema)**
```json
{
    "challenge_info": {
        "challenge_id": "round_1b_002",
        "test_case_name": "travel_planner",
        "description": "France Travel"
    },
    "documents": [
        {"filename": "South of France - Cities.pdf", "title": "South of France - Cities"},
        {"filename": "South of France - Cuisine.pdf", "title": "South of France - Cuisine"}
    ],
    "persona": { "role": "Travel Planner" },
    "job_to_be_done": { "task": "Plan a trip of 4 days for a group of 10 college friends." }
}
```

### **Output (JSON schema)**
```json
{
    "metadata": {
        "input_documents": ["South of France - Cities.pdf", "..."],
        "persona": "Travel Planner",
        "job_to_be_done": "Plan a trip of 4 days for a group of 10 college friends.",
        "processing_timestamp": "2025-07-10T15:31:22.632389"
    },
    "extracted_sections": [
        {
            "document": "South of France - Cities.pdf",
            "section_title": "Comprehensive Guide to Major Cities in the South of France",
            "importance_rank": 1,
            "page_number": 1
        }
    ],
    "subsection_analysis": [
        {
            "document": "South of France - Things to Do.pdf",
            "refined_text": "The South of France is renowned for its beautiful coastline...",
            "page_number": 2
        }
    ]
}
```

---


## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```
git clone https://github.com/SuhasMartha/Adobe-India-Hackathon25
cd Challenge_1b
```
### 2️⃣ Create Virtual Environment
```
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Parse Documents
```
python utils/pdf_parser.py "Inputs/Collection 1"
```
### 5️⃣ Extract Relevant Sections
```
python utils/extract_relevant.py "Inputs/Collection 1"
```

---


## 🐳 Docker Deployment
To build and run the solution using Docker:
### Build Image
```
docker build -t adobe-challenge-1b .
```
### Run Container
```
Run Container
```

---


## 📈 Performance
- ✅ CPU-only
- ✅ Model size ≤ 1GB
- ✅ Processes a collection in ≤ 60 seconds

---


## ✨ Deliverables
 - PDF parsing utility (pdf_parser.py)
 - Relevant section extraction (extract_relevant.py)
 - Dockerfile
 - Example input/output
 - README documentation
