# 📄 Adobe India Hackathon 2025 – Round 1A  
### **Understand Your Document Challenge**  
**Theme:** *Connecting the Dots Through Docs*

---

## 🚀 Overview
This repository contains our solution for **Round 1A of the Adobe India Hackathon 2025**.  
The challenge focuses on building an **intelligent document parser** that extracts a **structured outline** from PDFs.  

Our solution automatically identifies and organizes **Titles, Headings (H1, H2, H3)** along with their **page numbers**, outputting them in a **clean JSON format** for downstream processing.

---

## 🧠 Problem Statement
- Given a PDF document, the task is to:
  1. Understand its structure and hierarchy  
  2. Extract:
     - **Document Title**  
     - **Headings:** H1, H2, H3 (with nesting preserved)  
     - **Page numbers**  
  3. Output this information in a **structured JSON file**.

- The system must handle:
  - Multi-line headings  
  - Numbered headings  
  - Variable document formats (reports, guides, research papers, etc.)  

---

## 📂 Project Structure
```
Challenge_1a/
│── Inputs/ # PDF files for testing
│── Outputs/ # Generated JSON outputs
├── pdf_parser.py # Core PDF parsing logic
│── Dockerfile # Docker image for deployment
│── README.md # Project documentation
```

---

## ⚙️ Features
✅ Extracts **Title, H1, H2, H3** headings  
✅ Preserves **hierarchical structure**  
✅ Captures **page numbers** accurately  
✅ Handles **multi-line and numbered headings**  
✅ Exports structured **JSON output**  

---


## 🔑 Input & Output

### **Input**
- A single PDF document located in the `Inputs/` folder  

### **Output**
- JSON file saved in `Outputs/`:
```json
{
  "title": "Sample PDF Document",
  "headings": [
    {
      "text": "Chapter 1: Introduction",
      "level": "H1",
      "page": 1
    },
    {
      "text": "Background",
      "level": "H2",
      "page": 2
    }
  ]
}
```

---


## 🛠️ Setup Instructions
### 1️⃣ Clone the Repository
```
git clone https://github.com/SuhasMartha/Adobe-India-Hackathon25
cd Challenge_1a
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
### 4️⃣ Run PDF Parser
```
python utils/pdf_parser.py Inputs/sample.pdf
```

---


## 🐳 Docker Deployment
To build and run the solution using Docker:
### Build Image
```
docker build -t adobe-challenge-1a .
```
### Run Container
```
docker run -v $(pwd)/Inputs:/app/Inputs \
           -v $(pwd)/Outputs:/app/Outputs \
           adobe-challenge-1a
```

---


## 📈 Performance
- ✅ CPU-only execution
- ✅ Model size < 1GB
- ✅ Processes document in ≤ 30 seconds

---

## ✨ Deliverables
 - PDF parser code (pdf_parser.py)
 - Dockerfile
 - Example input/output
 - README documentation
