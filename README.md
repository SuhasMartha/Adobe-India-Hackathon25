# 🏆 Adobe India Hackathon 2025   

<p align="center">
  <img src="https://www.adobe.com/federal/assets/svgs/adobe-logo.svg" alt="Adobe Logo" width="200"/>
</p>
<p align="center">
  <b>Connecting the Dots...</b>
</p>


---

## 📌 Overview
This repository contains solutions for **Adobe India Hackathon 2025**, focusing on building **document understanding and persona-driven document intelligence** systems.

---

## 🔥 Rounds Overview

### **📄 Round 1A – Understand Your Document**  
**Theme:** *Connecting the Dots Through Docs*  
- Tasked with building a solution that **parses PDF documents** and extracts a **hierarchical document outline**.  
- Extracted structure includes:
  - **Title**
  - **H1, H2, H3 headings**
  - **Page numbers**  
- Output is a clean **JSON structure** representing document hierarchy.  

---

### **🤖 Round 1B – Persona-Driven Document Intelligence**  
**Theme:** *Connect What Matters — For the User Who Matters*  
- Extended solution to **analyze multiple related PDFs**.  
- Designed for a **specific persona** (e.g., Travel Planner) and their **job-to-be-done**.  
- System:
  - Parses PDFs
  - Ranks **important sections**
  - Produces **refined subsection analysis**
  - Outputs a final **structured JSON** with:
    - Metadata
    - Extracted sections
    - Subsection analysis  

---

## 📂 Repository Structure
```
Adobe-India-Hackathon25/
│── Challenge_1a/ # Round 1A solution
│ ├── Inputs/
│ ├── Outputs/
│ ├── Dockerfile
│ ├── extract_outline.py
│ ├── README.md
│── Challenge_1b/ # Round 1B solution
│ ├── Inputs/
│ ├── Outputs/
│ ├── utils/
│ │ ├── pdf_parser.py 
│ │ ├── extract_relevant.py 
│ ├── Dockerfile
│ ├── README.md
│── .gitignore
│── requirements.txt
│── README.md # This file
```

---

## ⚙️ Features
### ✅ Round 1A
- PDF parsing
- Heading hierarchy detection
- Output in structured JSON format

### ✅ Round 1B
- Multi-PDF persona-based analysis
- Section ranking & prioritization
- Refined text extraction for subsections
- Metadata-driven output

---

## 🔑 Input & Output

### **Round 1A Output (Sample)**:
```json
{
  "title": "Document Title",
  "headings": [
    {
      "level": "H1",
      "text": "Introduction",
      "page_number": 1
    },
    {
      "level": "H2",
      "text": "Background",
      "page_number": 2
    }
  ]
}
```
### **Round 1B Output (Sample)**:
```json
{
  "metadata": {
    "input_documents": ["Cities.pdf", "Cuisine.pdf"],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a trip of 4 days for 10 college friends",
    "processing_timestamp": "2025-07-10T15:31:22.632389"
  },
  "extracted_sections": [
    {
      "document": "Cities.pdf",
      "section_title": "Comprehensive Guide to Major Cities",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "Things to Do.pdf",
      "refined_text": "The South of France is renowned for its coastline...",
      "page_number": 2
    }
  ]
}
```

---
## 🛠️ Setup Instructions
### 1️⃣ Clone Repository
```
git clone https://github.com/SuhasMartha/Adobe-India-Hackathon25.git
cd Adobe-India-Hackathon25
```
### 2️⃣ Create Virtual Environment
```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

----

## ▶️ Running Solutions
### 🔹 Round 1A
```
cd Challenge_1a
python utils/pdf_parser.py "Inputs/Collection 1"
```
- Output is stored in ```Outputs/Collection 1/parsed.json```

### 🔹 Round 1B 
```
cd Challenge_1b
python utils/pdf_parser.py "Inputs/Collection 1"
python utils/extract_relevant.py "Inputs/Collection 1"
```
- Final JSON output is saved to ```Outputs/Collection 1/1b_output.json```

---

## 🐳 Docker Deployment
To run using Docker (works for both rounds):
### Build Image
```
docker build -t adobe-hackathon .
```
### Run Container
```
docker run -v $(pwd)/Challenge_1a/Inputs:/app/Inputs \
           -v $(pwd)/Challenge_1a/Outputs:/app/Outputs \
           adobe-hackathon
```

----

## 📈 Performance
- CPU-only solution
- Model size < 1GB
- Processes 3–5 PDFs in < 60 seconds

---

## ✨ Deliverables
- ✅ Round 1A & 1B solutions
- ✅ Dockerfiles
- ✅ Example inputs/outputs
- ✅ Documentation

---

## 🏆 Author
- 👤 [Suhas Martha](https://github.com/SuhasMartha)
- 👤 [Navaneeth Reddy](https://github.com/Navaneethreddy2004)
- 👤 [Harsha Vardhan Reddy](https://github.com/shreeharshareddy)

---

## 📝 License
This project is for the Adobe India Hackathon 2025 and follows competition rules.

---

<sub>Last Updated: 28-07-2025</sub>
