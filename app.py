import streamlit as st
import spacy
from pypdf import PdfReader

# load NLP model
nlp = spacy.load("en_core_web_sm")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Resume Text")

    st.write(text[:1000])

    doc = nlp(text)

    # skill list
    skill_keywords = [
        "python",
        "java",
        "c++",
        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "pytorch",
        "opencv",
        "react",
        "node",
        "sql",
        "data science",
    ]

    skills = []

    for token in doc:
        if token.text.lower() in skill_keywords:
            skills.append(token.text)

    skills = list(set(skills))

    st.subheader("Detected Skills")

    st.write(skills)

    # summary
    st.subheader("Resume Summary")

    sentences = list(doc.sents)

    summary = " ".join([str(sentences[i]) for i in range(min(3, len(sentences)))])

    st.write(summary)

    # suggestions
    st.subheader("Suggestions")

    text_lower = text.lower()

    if "python" not in text_lower:
        st.write("Consider adding Python projects")

    if "machine learning" not in text_lower:
        st.write("Add Machine Learning experience")

    if "deep learning" not in text_lower:
        st.write("Add Deep Learning projects")

    if "project" not in text_lower:
        st.write("Add project descriptions")

    st.write("Include measurable achievements in projects")
