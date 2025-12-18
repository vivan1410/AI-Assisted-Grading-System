from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def grade_answer(model_answer, student_answer):
    if not model_answer or not student_answer:
        return {
            "score": 0,
            "feedback": "Answer is empty"
        }

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([model_answer, student_answer])

    similarity = float(cosine_similarity(vectors[0], vectors[1])[0][0])
    marks = round(similarity * 10, 1)

    return {
        "score": marks,
        "feedback": "Marks calculated using TF-IDF similarity"
    }

