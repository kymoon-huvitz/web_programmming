from flask import Flask
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev_secret_key'  # Flask-WTF CSRF 보호용
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"   # 프로젝트 루트에 app.db 생성
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 확장 초기화
    db.init_app(app)
    login_manager.init_app(app)

    # --- 블루프린트 등록 ---
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # 실서비스에선 Alembic(Migrate) 권장이지만, 지금은 **학습용 create_all()**로 충분.
    with app.app_context():
        db.create_all()

    return app

# Flask-Login이 user_id로 유저를 복구할 때 사용하는 로더
from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))