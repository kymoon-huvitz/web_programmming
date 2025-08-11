import os
from flask import Flask
from .extensions import db, login_manager

def create_app(config_object='config.DevConfig'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    os.makedirs(app.instance_path, exist_ok=True)

    # 확장 초기화
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # 🔽 여기서 User를 import 해야 user_loader가 User를 볼 수 있습니다.
    from .models import User

    # 🔽 user_loader 등록 (세션의 user_id → User 객체로 복원)
    @login_manager.user_loader
    def load_user(user_id: str):
        # SQLAlchemy 2.x 권장 방식
        return db.session.get(User, int(user_id))

    # 블루프린트 등록
    from .routes.auth import auth_bp
    from .routes.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app