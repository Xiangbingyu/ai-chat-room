from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    """创建Flask应用实例"""
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object('app.config.Config')
    
    # 初始化扩展
    CORS(app)
    
    # 注册蓝图
    from app.api.db import db_bp
    from app.api.llm import llm_bp
    app.register_blueprint(db_bp)
    app.register_blueprint(llm_bp)
    
    # 健康检查路由
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}
    
    return app
