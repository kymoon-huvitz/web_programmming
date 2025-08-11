from flask import Flask, request, jsonify
from json import JSONDecodeError
from pathlib import Path

import json
import os
import tempfile

# static 폴더를 정적 폴더로 지정하여 HTML/JS/CSS 서빙
app = Flask(__name__, static_folder="static", static_url_path="")

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

# 데이터 불러오기
def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
    
# 데이터 저장하기
def save_data(data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(DATA_FILE.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, DATA_FILE)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise

@app.route("/ping")
def ping():
    return {"status": "ok"}

# 방명록 목록 조회
@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(load_data())

# 방명록 새 글 작성
@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json(silent=True) or {}
    messages = load_data()
    name = (data.get("name") or "익명").strip()
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "message is required"}), 400
    messages.append({"name": name[:50], "message": message[:500]})
    save_data(messages)
    return jsonify({"status": "success"}), 201

# 루트로 접속 시 index.html 서빙
@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    if not DATA_FILE.exists():
        save_data([])
    app.run(debug=True)