from flask import Flask  # Flask 클래스 불러오기

app = Flask(__name__)    # Flask 앱 생성

@app.route("/")          # '/' URL에 접속하면 실행될 함수 등록
def home():
    return "Hello, Flask!"  # 브라우저에 이 문구가 보임

if __name__ == "__main__":
    app.run(debug=True)  # 서버 실행 (debug=True → 코드 변경 시 자동 재시작)