"""
config.py — 설정 모음
- 환경변수로 덮어쓸 수 있도록 기본값을 제공.
"""
import os

class BaseConfig:
    # 운영환경에서는 반드시 환경변수로 SECRET_KEY 를 지정하세요.
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-me')
    # DATABASE_URL 이 지정되지 않았으면 SQLite 로 동작합니다.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    DEBUG = True
