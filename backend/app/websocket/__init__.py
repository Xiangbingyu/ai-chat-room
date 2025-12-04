from flask_socketio import SocketIO

# 创建SocketIO实例
socketio = SocketIO(cors_allowed_origins="*")

# 导入所有事件处理函数
from app.websocket.events import *
