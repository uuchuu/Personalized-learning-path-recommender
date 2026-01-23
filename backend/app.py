from flask import Flask, jsonify
from algorithm.path_recommender import recommend_learning_path

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"system": "Personalized Learning Path Recommendation System"})

@app.route("/recommend/<int:student_id>")
def recommend(student_id):
    # 模拟数据库数据
    courses = {
        1: "Programming Basics",
        2: "Data Structures",
        3: "Database Systems",
        4: "Machine Learning"
    }

    prerequisites = [
        (2, 1),
        (3, 2),
        (4, 3)
    ]

    learned_courses = {1}
    target = "AI"

    path = recommend_learning_path(
        courses,
        prerequisites,
        learned_courses,
        target=target
    )

    return jsonify({
        "student_id": student_id,
        "target": target,
        "recommended_path": path
    })

if __name__ == "__main__":
    app.run(debug=True)
