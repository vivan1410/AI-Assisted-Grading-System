'''from sklearn.feature_extraction.text import TfidfVectorizer
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
    }'''

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def grade_answer(question, model_answer, student_answer, max_marks=10):
    if not student_answer.strip():
        return {
            "score": 0,
            "feedback": "No answer submitted."
        }

    # TF-IDF similarity
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )
    vectors = vectorizer.fit_transform([
        model_answer,
        student_answer
    ])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    score = round(similarity * max_marks, 1)

    # AI-style feedback
    if score >= 0.85 * max_marks:
        feedback = "Excellent answer. Key concepts are clearly explained."
    elif score >= 0.6 * max_marks:
        feedback = "Good answer, but some important points are missing."
    elif score >= 0.3 * max_marks:
        feedback = "Partial understanding shown. Needs improvement."
    else:
        feedback = "Answer does not address the main concepts."

    return {
        "score": score,
        "feedback": feedback
    }

