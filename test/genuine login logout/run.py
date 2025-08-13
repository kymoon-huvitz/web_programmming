"""
run.py — 애플리케이션 '시동키' (엔트리포인트)
- 이 파일을 실행하면 Flask 앱이 만들어지고, 로컬 개발 서버가 뜹니다.
- Docker/운영에서는 gunicorn이 이 파일의 `app` 객체를 로딩합니다 (예: run:app).
"""

from app import create_app                 # 앱을 만들어주는 '공장 함수'를 가져옵니다.
from app.extensions import db              # 데이터베이스 객체 (SQLAlchemy)

# create_app() 에게 어떤 설정 클래스를 쓸지 문자열로 넘깁니다.
# config.py 안의 DevConfig 를 사용하게 됩니다.
app = create_app('config.DevConfig')

if __name__ == '__main__':
    # Flask 3.x 에서는 before_first_request 훅이 제거되었으므로
    # 앱 컨텍스트를 열고 테이블을 선행 생성합니다.
    with app.app_context():
        db.create_all()    # models.py 에 정의된 모든 테이블 생성 (존재하면 스킵)
    # 개발 서버 실행 (운영에서는 gunicorn 사용)
    app.run(host='127.0.0.1', port=8000, debug=True)
