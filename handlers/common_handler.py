# File: handlers/common_handler.py
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters  

async def start(update: Update, context: CallbackContext):
    buttons = [
        ["📦 New Shipment"],
        ["📋 View All Shipments"],
        ["🔍 View by ID"],
        ["🆘 Help"]
    ]
    await update.message.reply_text(
        "🤖 User Guide:\n"
        "1. New Shipment: Create a new shipment record\n"
        "2. View All Shipment: Browse all shipments\n"
        "3. View by ID: Query details by shipment ID\n"
        "4. Help: Display this help information\n\n"
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/cancel - Cancel the current action\n"
        "/next - Go to the next page\n"
        "/previous - Go to the previous page",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

async def help(update, context):
    """显示帮助信息"""
    help_text = (
        "🤖 User Guide:\n"
        "1. New Shipment: Create a new shipment record\n"
        "2. View All Shipment: Browse all shipments\n"
        "3. View by ID: Query details by shipment ID\n"
        "4. Help: Display this help information\n\n"
        "Here are the available commands:\n"
        "/start - Start the bot\n"
        "/cancel - Cancel the current action\n"
        "/next - Go to the next page\n"
        "/previous - Go to the previous page"
    )
    await update.message.reply_text(help_text)


def setup_common_handlers(app):
    """注册通用处理器"""
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(MessageHandler(filters.Regex(r"^🆘 Help$"), help))