"""
app/extensions.py — 확장 인스턴스 중앙 관리
- 실제 앱과 결합은 __init__.py에서 init_app() 으로 이뤄집니다.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()          # ORM (데이터베이스 접근을 파이썬 객체로)
login_manager = LoginManager()  # 로그인/세션 관리
