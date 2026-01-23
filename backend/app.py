from flask import Flask, jsonify
from algorithm.path_recommender import recommend_learning_path

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Personalized Learning Path Recommender Backend Running"
    })

@app.route("/recommend")
def recommend():
    # 模拟数据库中的课程数据
    courses = {
        1: "Programming Basics",
        2: "Data Structures",
        3: "Database Systems",
        4: "Machine Learning"
    }

    # 课程先修关系（有向边）
    prerequisites = [
        (2, 1),
        (3, 2),
        (4, 3)
    ]

    # 假设学生已经学过课程 1
    learned_courses = {1}

    path = recommend_learning_path(courses, prerequisites, learned_courses)

    return jsonify({
        "recommended_path": path
    })

if __name__ == "__main__":
    app.run(debug=True)
