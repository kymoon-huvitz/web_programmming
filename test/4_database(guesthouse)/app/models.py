from datetime import datetime, timezone
from app.extensions import db

class GuestbookEntry(db.Model):
    __tablename__ = 'guestbook_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False) #이름
    message = db.Column(db.Text, nullable=False) #내용
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc)) #작성 시간 (UTC)

    def __repr__(self):
        return f"<GuestbookEntry {self.id} - {self.name}>"