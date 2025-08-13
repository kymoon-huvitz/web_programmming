from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev_secret_key'  # Flask-WTF CSRF 보호용
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"   # 프로젝트 루트에 app.db 생성
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 확장 초기화
    db.init_app(app)

    # 라우트 등록
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    # 실서비스에선 Alembic(Migrate) 권장이지만, 지금은 **학습용 create_all()**로 충분.
    with app.app_context():
        db.create_all()

    return app