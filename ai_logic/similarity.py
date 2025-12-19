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


def grade_answer(question, model_answer, student_answer, max_marks):
    # Convert to lowercase and strip spaces
    model_answer = model_answer.lower().strip()
    student_answer = student_answer.lower().strip()

    # If student didn't answer
    if not student_answer:
        return {
            "score": 0,
            "feedback": "No answer submitted."
        }

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([model_answer, student_answer])

    # Cosine similarity
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Convert similarity to marks
    score = round(similarity * max_marks)

    # Simple feedback
    if similarity < 0.2:
        feedback = "Answer is not relevant."
    elif similarity < 0.5:
        feedback = "Partially correct answer."
    elif similarity < 0.8:
        feedback = "Good answer."
    else:
        feedback = "Excellent answer."

    return {
        "score": score,
        "feedback": feedback
    }
