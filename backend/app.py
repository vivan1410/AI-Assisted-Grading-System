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

# ✅ FORCE Python to see project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ai_logic.similarity import grade_answer

app = Flask(__name__, template_folder="../templates")
CORS(app)

QUESTION = "Explain the process of photosynthesis."
MODEL_ANSWER = (
    "Photosynthesis is the process by which green plants use sunlight "
    "to synthesize food from carbon dioxide and water using chlorophyll."
)
MAX_MARKS = 10

@app.route("/")
def home():
    return render_template("index.html", question=QUESTION)

@app.route("/grade", methods=["POST"])
def grade():
    data = request.json

    result = grade_answer(
        QUESTION,
        MODEL_ANSWER,
        data["student_answer"],
        MAX_MARKS
    )

    return jsonify({
        "roll_no": data["roll_no"],
        "score": result["score"],
        "feedback": result["feedback"]
    })

if __name__ == "__main__":
    print("AI Grading Server Running...")
    app.run(debug=True)
