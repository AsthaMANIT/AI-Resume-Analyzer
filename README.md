AI Resume Analyzer--

AI Resume Analyzer is a simple AI-powered application that analyzes resumes and provides useful insights. The system extracts text from uploaded PDF resumes, detects technical skills using Natural Language Processing (NLP), generates a summary, and provides suggestions for improving the resume.

This project demonstrates how AI and NLP techniques can be used to analyze real-world documents and help job seekers improve their resumes.

Features--

Upload resume in PDF format

Extract text from resume

Detect technical skills automatically

Generate a short resume summary

Provide suggestions for improving the resume

Technologies Used--

Python

Streamlit

spaCy (Natural Language Processing)

PyPDF (PDF text extraction)

Project Structure--
resume_analyzer
│
├── app.py
├── README.md

Installation--

Clone the repository:

git clone https://github.com/yourusername/ai-resume-analyzer.git

Go to the project folder:

cd ai-resume-analyzer

Install dependencies:

pip install streamlit spacy pypdf

Download the spaCy model:

python -m spacy download en_core_web_sm
Run the Application

Run the Streamlit application:

streamlit run app.py

Open your browser and go to:

http://localhost:8501

How It Works----

The user uploads a resume in PDF format.

The system extracts text from the PDF file.

spaCy NLP processes the text to detect technical skills.

The system generates a short summary of the resume.

Suggestions are provided to help improve the resume.

Example Output-----

Detected Skills-

Python
TensorFlow
React
NLP

Resume Summary-

A highly motivated AI and Machine Learning enthusiast with experience in Python, deep learning, and computer vision.

Suggestions-

Include measurable achievements in projects
Add more project descriptions
Future Improvements

Resume ATS scoring

Job description matching

Advanced skill detection using machine learning

Resume analytics dashboard
