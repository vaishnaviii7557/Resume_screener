from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def rank_resumes(jd_embedding, resume_embeddings, resume_names):
    scores = cosine_similarity(
        [jd_embedding],
        resume_embeddings
    )[0]
    
    ranked = sorted(
        zip(resume_names, scores),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked