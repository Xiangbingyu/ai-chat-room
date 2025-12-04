from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 创建数据库实例
db = SQLAlchemy()

# 导入所有模型
from app.models.room import Room
from app.models.character import Character
from app.models.conversation import Conversation
