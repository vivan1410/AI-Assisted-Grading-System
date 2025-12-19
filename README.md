# AI Assisted Grading System

Project Description
The AI Assisted Grading System is a web-based application that automatically evaluates descriptive answers written by students.  
It uses TF-IDF and Cosine Similarity to compare a student’s answer with a model answer and assigns marks accordingly.

This system reduces manual evaluation effort and provides instant feedback.

---

Objectives
- Automate answer evaluation
- Reduce human bias in grading
- Provide instant feedback to students
- Assist teachers in managing assessments efficiently

---

Features
- Staff can add questions with model answers and total marks
- Students can select questions and submit answers
- Automatic grading using NLP techniques
- Instant score and feedback generation
- Web-based interface using Flask

---

Technologies Used
- Backend: Python, Flask
- AI / NLP: TF-IDF, Cosine Similarity (scikit-learn)
- Frontend: HTML, JavaScript
- Others: Flask-CORS

---

Project Structure
The project is organized into different folders, each having a specific purpose.

ai_logic
This folder contains the AI logic used for grading answers.
The similarity.py file implements TF-IDF and cosine similarity to evaluate student answers.

backend
This folder contains the backend code of the application.
The app.py file is a Flask application that handles routing, question management, and grading requests.

templates
This folder contains all the HTML files used for the user interface.

index.html is the home page where users select their role.

staff.html allows staff to add questions, model answers, and marks.

student.html allows students to submit answers and view scores and feedback.

README.md
This file provides an overview of the project, instructions to run the application, and details about the technologies used.
