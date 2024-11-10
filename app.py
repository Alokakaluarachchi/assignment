from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)

# Load questions from JSON file with UTF-8 encoding
with open("stock_data.json", encoding="utf-8") as f:
    questions = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit_quiz():
    user_answers = request.form.to_dict()
    score = 0
    results = []

    for question in questions:
        question_id = str(question["id"])
        correct_answer = question["answerKey"]
        user_answer = user_answers.get(question_id)
        
        is_correct = user_answer == correct_answer
        if is_correct:
            score += 1
        
        results.append({
            "question": question["question"],
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        })

    return render_template("summary.html", score=score, total=len(questions), results=results)

if __name__ == "__main__":
    app.run(debug=True)
