from app.models import db
from datetime import datetime

# 对话模型
class Conversation(db.Model):
    __tablename__ = 'conversation'
    
    id = db.Column(db.String(50), primary_key=True)
    room_id = db.Column(db.String(50), db.ForeignKey('room.id'), nullable=False)
    character_id = db.Column(db.String(50), db.ForeignKey('character.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
