from app import create_app

# Flask 애플리케이션 생성
app = create_app()

if __name__ == "__main__":
    # debug=True → 코드 변경 시 자동 리로드 & 에러 화면 제공
    app.run(debug=True)