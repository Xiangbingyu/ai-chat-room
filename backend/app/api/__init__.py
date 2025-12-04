# API蓝图注册
from app.api.db import db_bp
from app.api.llm import llm_bp

__all__ = ['db_bp', 'llm_bp']
