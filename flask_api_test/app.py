from flask import Flask, request, jsonify

app = Flask(__name__)

# 메모리 내 임시 데이터 저장소
messages = []

# ✅ GET: 전체 메시지 보기
@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

# ✅ POST: 메시지 추가
@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json()  # JSON 요청 받기
    message = {
        "name": data.get("name"),
        "message": data.get("message")
    }
    messages.append(message)
    return jsonify({"status": "success", "data": message}), 201

if __name__ == "__main__":
    app.run(debug=True)