"""
app/models.py — 데이터베이스 모델(테이블 구조)
- User 테이블: 이메일과 비밀번호(해시) 보관
"""
from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)                 # 기본키
    email = db.Column(db.String(255), unique=True, nullable=False)  # 이메일 (고유)
    password_hash = db.Column(db.String(255), nullable=False)    # 비밀번호 해시

    def set_password(self, password: str) -> None:
        """
        평문 비밀번호를 안전한 해시로 바꿔서 저장합니다.
        - 해시 함수는 일방향: 원래 비밀번호를 복구할 수 없습니다.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        입력한 평문 비밀번호와 저장된 해시가 같은지 확인합니다.
        """
        return check_password_hash(self.password_hash, password)
