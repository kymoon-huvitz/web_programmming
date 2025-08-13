from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = "auth.login"  # 인증 필요한 페이지 접근 시 보내줄 엔드포인트
login_manager.login_message = "로그인이 필요합니다."