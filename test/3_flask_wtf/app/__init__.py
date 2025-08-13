from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev_secret_key'  # Flask-WTF CSRF 보호용

    # 라우트 등록
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app