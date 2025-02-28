import os
from dotenv import load_dotenv
from telegram.ext import Application
from handlers import (
    setup_common_handlers,
    setup_create_handlers,
    setup_view_handlers
)

load_dotenv()

def main():
    app = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    
    # 设置各模块处理器
    setup_common_handlers(app)
    setup_create_handlers(app)
    setup_view_handlers(app)

    app.run_polling()

if __name__ == "__main__":
    main()