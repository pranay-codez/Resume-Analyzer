# Resume Analyzer

A Python-based AI Resume Analyzer that extracts text from PDF resumes and uses a locally running Ollama LLM to generate structured feedback.

## Features

- Accepts PDF resumes
- Extracts text from multiple pages using PyPDF
- Allows custom analysis context and tasks
- Uses Ollama and Llama 3.2 for analysis
- Generates a structured resume analysis report
- Saves the result to a text file
- Supports resumes located outside the project directory

## Technologies

- Python
- PyPDF
- Ollama
- Llama 3.2

## Workflow

PDF Resume
↓
PyPDF Text Extraction
↓
Prompt Construction
↓
Ollama / Llama 3.2
↓
Resume Analysis
↓
Report.txt

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt