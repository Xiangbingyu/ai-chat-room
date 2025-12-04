from app.main import create_app
from app.models import db
from app.websocket import socketio

app = create_app()

db.init_app(app)
socketio.init_app(app)

# 确保在应用启动时创建数据库表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
