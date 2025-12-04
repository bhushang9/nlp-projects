import streamlit as st
from pdf_reader import extract_text_from_pdf, extract_text_from_txt
from summarize import generate_summary  
from mcq_generator import generate_mcqs  # now returns structured MCQs list

st.title("📘 MCQ + Summary Generator")

uploaded_file = st.file_uploader("Upload PDF/TXT", type=["pdf","txt"])

if uploaded_file:
    text = (extract_text_from_pdf(uploaded_file) 
            if uploaded_file.name.endswith(".pdf") 
            else extract_text_from_txt(uploaded_file))

    st.subheader("Extracted Text:")
    st.write(text[:800] + "..." if len(text)>800 else text)

    # SUMMARY SECTION
    if st.button("Generate Summary"):
        with st.spinner("Generating Summary..."):
            summary = generate_summary(text)
        st.subheader("📌 Summary")
        st.write(summary)

    # MCQ SECTION
    if st.button("Generate MCQs"):
        with st.spinner("Generating MCQs..."):
            mcqs = generate_mcqs(text)  # returns list of dicts

        st.subheader("📝 MCQs")
        for i, mcq in enumerate(mcqs, 1):
            st.markdown(f"""
**{mcq['question']}**

A) {mcq['A'][3:].strip() if mcq['A'].startswith('A)') else mcq['A']}  
B) {mcq['B'][3:].strip() if mcq['B'].startswith('B)') else mcq['B']}  
C) {mcq['C'][3:].strip() if mcq['C'].startswith('C)') else mcq['C']}  
D) {mcq['D'][3:].strip() if mcq['D'].startswith('D)') else mcq['D']}  

**Answer:** {mcq['answer'].replace("Answer:", "").strip()}
            """)
            st.write("---")
