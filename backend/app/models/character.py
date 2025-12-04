from app.models import db
from datetime import datetime

# 人物模型
class Character(db.Model):
    __tablename__ = 'character'
    
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    room_id = db.Column(db.String(50), db.ForeignKey('room.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
