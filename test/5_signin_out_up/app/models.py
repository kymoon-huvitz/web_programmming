from datetime import datetime, timezone
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

class GuestbookEntry(db.Model):
    __tablename__ = 'guestbook_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False) #이름
    message = db.Column(db.Text, nullable=False) #내용
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc)) #작성 시간 (UTC)

    def __repr__(self):
        return f"<GuestbookEntry {self.id} - {self.name}>"
    
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str):
        # 기본: pbkdf2:sha256
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"