# File: handlers/__init__.py
from .create_handler import setup_create_handlers
from .view_handler import setup_view_handlers
from .common_handler import setup_common_handlers

def setup_handlers(app):
    """注册所有处理器"""
    setup_common_handlers(app)
    setup_create_handlers(app)
    setup_view_handlers(app)