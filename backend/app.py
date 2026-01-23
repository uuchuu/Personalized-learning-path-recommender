from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Personalized Learning Path Recommender Backend Running"
    })

@app.route("/recommend")
def recommend():
    # 先写死一条推荐结果，后面再换成算法
    return jsonify({
        "recommended_path": [
            "Programming Basics",
            "Data Structures",
            "Database Systems"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)

