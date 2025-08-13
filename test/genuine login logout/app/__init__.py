"""
app/__init__.py — 애플리케이션 팩토리(공장) + 배선
- Flask 확장 초기화, 블루프린트 등록, 로그인 로더 등을 여기서 설정합니다.
"""
import os
from flask import Flask
from .extensions import db, login_manager   # 공용 확장 인스턴스
                                            
def create_app(config_object: str = 'config.DevConfig'):
    """
    Flask 애플리케이션을 생성해서 반환합니다.
    config_object: '모듈.클래스' 형태의 문자열 (예: 'config.DevConfig')
    """
    # instance_relative_config=True 로 두면,
    # app.instance_path 가 프로젝트 내부의 'instance' 폴더로 잡혀서
    # SQLite 파일/비밀 키 등 런타임 데이터를 분리 보관하기 좋습니다.
    app = Flask(__name__, instance_relative_config=True)

    # 1) 설정 로딩
    app.config.from_object(config_object)

    # 2) instance 폴더 보장 (존재하지 않으면 생성)
    #    Docker 비루트 유저로 실행할 때 권한 문제가 나면
    #    Dockerfile에서 /app 전체를 해당 유저 소유로 chown 하세요.
    os.makedirs(app.instance_path, exist_ok=True)

    # 3) 확장 초기화
    db.init_app(app)
    login_manager.init_app(app)

    # 로그인 안 된 사용자가 보호된 페이지 접근 시 보내줄 엔드포인트명
    login_manager.login_view = 'auth.login'

    # 4) Flask-Login: 세션의 user_id -> 실제 User 객체로 복원
    #    이 함수가 등록되어 있어야 current_user 가 동작합니다.
    from .models import User

    @login_manager.user_loader
    def load_user(user_id: str):
        # SQLAlchemy 2.x 스타일: db.session.get(모델, 기본키)
        return db.session.get(User, int(user_id))

    # 5) 블루프린트(라우트 묶음) 등록
    from .routes.auth import auth_bp
    from .routes.main import main_bp
    app.register_blueprint(auth_bp)   # /register, /login, /logout
    app.register_blueprint(main_bp)   # /, /dashboard

    return app
