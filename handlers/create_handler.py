from telegram.ext import (
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    filters,
)
from services.google_drive import GoogleDriveService
from services.google_sheets import GoogleSheetService
from utils.helpers import generate_shipment_id
from database import Database
import datetime

# 对话状态
(CUSTOMER_NAME, ADDRESS, TRACKING_NUMBER, PHOTOS) = range(4)

db = Database()
drive_service = GoogleDriveService()
sheet_service = GoogleSheetService()

async def start_creation(update, context):
    """启动创建货件流程"""
    context.user_data.clear()
    await update.message.reply_text("📝 Please enter the customer's name:")
    return CUSTOMER_NAME

async def handle_customer_name(update, context):
    """处理客户姓名输入"""
    context.user_data["customer_name"] = update.message.text
    await update.message.reply_text("🏠 Please enter the delivery address:")
    return ADDRESS

async def handle_address(update, context):
    """处理地址输入"""
    context.user_data["address"] = update.message.text
    await update.message.reply_text("📮 Please enter the tracking number:")
    return TRACKING_NUMBER

async def handle_tracking_number(update, context):
    """处理运单号输入"""
    context.user_data["tracking_number"] = update.message.text
    await update.message.reply_text("📸 Please upload photos (up to 3, enter /done to finish):")
    return PHOTOS

async def handle_photo(update, context):
    """处理照片上传"""
        
    if len(context.user_data.get("photos", [])) >= 3:
        await update.message.reply_text("⚠️ You can upload a maximum of 3 photos. Enter /done to finish.")
        return PHOTOS
    
    photo_file = await update.message.photo[-1].get_file()
    photo_bytes = await photo_file.download_as_bytearray()
    
    # 生成货件ID并上传
    shipment_id = generate_shipment_id()
    photo_url = drive_service.upload_photo(photo_bytes, shipment_id)
    
    context.user_data.setdefault("photos", []).append(photo_url)
    await update.message.reply_text(f"✅ Photo uploaded ({len(context.user_data['photos'])}/3)")
    return PHOTOS


async def finalize_creation(update, context):
    """完成创建流程"""
    try:
        # Prepare shipment data
        shipment_data = {
            "shipment_id": generate_shipment_id(),
            **context.user_data,  # Spread context user data
            "status": "Pending Review",  # Default status
            "created_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Add created_at
            "updated_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Add updated_at
        }

        # Call the create_shipment method to store the shipment data
        db.create_shipment(shipment_data)
        
        # Notify the user of success
        await update.message.reply_text("🎉 Shipment created successfully!")
    except Exception as e:
        # Handle any errors during creation
        await update.message.reply_text(f"❌ Creation failed: {str(e)}")
    finally:
        # Clear the user data to reset the process
        context.user_data.clear()
    
    return ConversationHandler.END


async def cancel_creation(update, context):
    """取消创建流程"""
    await update.message.reply_text("❌ Shipment creation process canceled.")
    context.user_data.clear()
    return ConversationHandler.END

def setup_create_handlers(app):
    """注册创建货件处理器"""
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex(r"^📦 New Shipment$"), start_creation)],
        states={
            CUSTOMER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_customer_name)],
            ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address)],
            TRACKING_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tracking_number)],
            PHOTOS: [
                MessageHandler(filters.PHOTO, handle_photo),
                CommandHandler("done", finalize_creation),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel_creation)],
    )
    app.add_handler(conv_handler)