'''import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from ai_logic.similarity import grade_answer

app = Flask(__name__,template_folder="../templates")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grade", methods=["POST"])
def grade():
    data = request.json
    model_answer = data.get("model_answer")
    student_answer = data.get("student_answer")

    result = grade_answer(model_answer, student_answer)
    return jsonify(result)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)'''
import sys
import os

# ---------------- PATH FIX ---------------- #
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ai_logic.similarity import grade_answer

# ---------------- APP SETUP ---------------- #
app = Flask(
    __name__,
    template_folder=os.path.join(PROJECT_ROOT, "templates")
)
CORS(app)

# ---------------- IN-MEMORY STORE ---------------- #
# questions = {
#   "1": {
#       "question": "...",
#       "model_answer": "...",
#       "marks": 10
#   }
# }
questions = {}

# ---------------- PAGE ROUTES ---------------- #

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")

@app.route("/student")
def student():
    # IMPORTANT: pass questions to student page
    return render_template("student.html", questions=questions)

# ---------------- API ROUTES ---------------- #

@app.route("/add_question", methods=["POST"])
def add_question():
    data = request.get_json()

    qid = str(data["question_id"])

    questions[qid] = {
        "question": data["question"],
        "model_answer": data["model_answer"],
        "marks": int(data["marks"])
    }

    print("Question Added:", questions[qid])  # visible in terminal

    return jsonify({"status": "success"})

@app.route("/grade", methods=["POST"])
def grade():
    try:
        data = request.get_json()

        qid = str(data["question_id"])
        student_answer = data["student_answer"].strip()

        if qid not in questions:
            return jsonify({
                "score": 0,
                "feedback": "Invalid question selected"
            })

        q = questions[qid]

        result = grade_answer(
            q["question"],
            q["model_answer"],
            student_answer,
            q["marks"]
        )

        return jsonify({
            "score": result["score"],
            "feedback": result["feedback"]
        })

    except Exception as e:
        print("ERROR IN /grade:", e)
        return jsonify({
            "score": 0,
            "feedback": "Error while grading"
        }), 500

# ---------------- RUN SERVER ---------------- #

if __name__ == "__main__":
    print("AI Grading Server Running...")
    app.run(debug=True)
