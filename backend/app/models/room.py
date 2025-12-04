from app.models import db
from datetime import datetime

# 房间模型
class Room(db.Model):
    __tablename__ = 'room'
    
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    worldview = db.Column(db.Text)  # 世界观字段
    created_at = db.Column(db.DateTime, default=db.func.now())
