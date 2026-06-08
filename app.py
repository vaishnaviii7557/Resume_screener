import streamlit as st
from parser import extract_text
from embedder import get_embedding
from scorer import rank_resumes

st.title("Resume Screener")
st.subheader("Upload Job Description + Resumes")

jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")
resume_files = st.file_uploader("Upload Resumes (PDF)", 
                                 type="pdf", 
                                 accept_multiple_files=True)

if st.button("Rank Resumes"):
    if not jd_file or not resume_files:
        st.warning("Please upload JD and at least one resume.")
    else:
        with st.spinner("Processing..."):
            jd_text = extract_text(jd_file)
            
            resume_texts = []
            resume_names = []
            for r in resume_files:
                resume_texts.append(extract_text(r))
                resume_names.append(r.name)
            
            jd_embedding = get_embedding(jd_text)
            resume_embeddings = [get_embedding(t) for t in resume_texts]
            
            results = rank_resumes(jd_embedding, 
                                   resume_embeddings, 
                                   resume_names)
            
            st.success("Done! Here are the results:")
            for rank, (name, score) in enumerate(results, 1):
                st.write(f"**#{rank} — {name}** | Score: `{round(float(score)*100, 2)}%`")