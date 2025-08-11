from app import create_app
from app.extensions import db

app = create_app('config.DevConfig')

if __name__ == '__main__':
    # Flask 3.x: 서버 시작 전 테이블 생성
    with app.app_context():
        db.create_all()
    app.run()