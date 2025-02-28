# # File: handlers/view_handler.py
# from telegram import Update, ReplyKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters  
# from database import Database

# db = Database()

# async def handle_view_all(update, context):
#     """View all shipments"""
#     # Fetch all shipment records from the database
#     shipments = db.get_all_shipments()  # Assuming this method fetches all shipments
#     if not shipments:
#         await update.message.reply_text("❌ No shipments found.")
#         return

#     # Sort the shipments by 'created_at' in descending order
#     shipments.sort(key=lambda x: x['created_at'], reverse=True)

#     # Paginate the results (this example shows 5 shipments per page)
#     shipments_per_page = 5
#     total_pages = (len(shipments) + shipments_per_page - 1) // shipments_per_page  # Calculate the total number of pages

#     # Store the current page in user data (to remember across multiple messages)
#     current_page = context.user_data.get('current_page', 1)

#     # Determine which shipments to display for the current page
#     start_index = (current_page - 1) * shipments_per_page
#     end_index = min(current_page * shipments_per_page, len(shipments))
#     page_shipments = shipments[start_index:end_index]

#     # Create a response for the current page of shipments
#     response = "📋 All Shipments:\n"
#     for shipment in page_shipments:
#         response += (
#             f"📦 Shipment ID: {shipment.get('Shipment ID', 'N/A')}\n"
#             f"👤 Customer: {shipment.get('Customer Name', 'N/A')}\n"
#             f"🏠 Address: {shipment.get('Address', 'N/A')}\n"
#             f"📮 Tracking Number: {shipment.get('Tracking Number', 'N/A')}\n"
#             f"📷 Photos: {shipment.get('Photos', 'N/A')}\n"
#             f"📅 Created At: {shipment['created_at']}\n"
#             f"🔄 Updated At: {shipment['updated_at']}\n\n"
#         )

#     # Add pagination controls (Next/Previous)
#     pagination_controls = ""
#     if current_page > 1:
#         pagination_controls += "/previous - Previous Page\n"
#     if current_page < total_pages:
#         pagination_controls += "/next - Next Page"

#     await update.message.reply_text(response + pagination_controls)

# async def handle_view_by_id(update, context):
#     """按ID查看货件"""
#     await update.message.reply_text("🔍 Please enter the shipment ID:")

# async def handle_shipment_id(update, context):
#     """处理货件ID输入"""
#     shipment_id = update.message.text
#     shipment = db.get_shipment(shipment_id)
#     if shipment:
#         response = (
#             f"📦 Shipment ID: {shipment[0]}\n"
#             f"👤 Customer: {shipment[1]}\n"
#             f"🏠 Address: {shipment[2]}\n"
#             f"📮 Tracking Number: {shipment[3]}\n"
#             f"📷 Photos: {shipment[4]}\n"
#             f"📅 Created At: {shipment[6]}\n"
#             f"🔄 Updated At: {shipment[7]}"
#         )
#     else:
#         response = "❌ Shipment not found"
#     await update.message.reply_text(response)


# async def handle_previous_page(update, context):
#     """Go to the previous page"""
#     current_page = context.user_data.get('current_page', 1)
#     current_page = max(1, current_page - 1)  # Ensure page does not go below 1
#     context.user_data['current_page'] = current_page

#     # Call the `handle_view_all` function again to show the previous page of results
#     await handle_view_all(update, context)


# async def handle_next_page(update, context):
#     """Go to the next page"""
#     current_page = context.user_data.get('current_page', 1)
#     current_page += 1
#     context.user_data['current_page'] = current_page

#     # Call the `handle_view_all` function again to show the next page of results
#     await handle_view_all(update, context)


# def setup_view_handlers(app):
#     """注册查看货件处理器"""
#     app.add_handler(MessageHandler(filters.Regex(r"^📋 View All Shipments$"), handle_view_all))
#     app.add_handler(MessageHandler(filters.Regex(r"^🔍 View by ID$"), handle_view_by_id))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_shipment_id))
#     app.add_handler(CommandHandler("next", handle_next_page))  # Handler for next page
#     app.add_handler(CommandHandler("previous", handle_previous_page)) 

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, ConversationHandler
from database import Database

db = Database()

# Define a state for viewing by ID
VIEW_BY_ID = 0

async def handle_view_all(update, context):
    """View all shipments"""
    # Fetch all shipment records from the database
    shipments = db.get_all_shipments()  # Assuming this method fetches all shipments
    if not shipments:
        await update.message.reply_text("❌ No shipments found.")
        return

    # Sort the shipments by 'created_at' in descending order
    shipments.sort(key=lambda x: x['created_at'], reverse=True)
    
    # Paginate the results (this example shows 5 shipments per page)
    shipments_per_page = 5
    total_pages = (len(shipments) + shipments_per_page - 1) // shipments_per_page  # Calculate the total number of pages

    # Store the current page in user data (to remember across multiple messages)
    current_page = context.user_data.get('current_page', 1)

    # Determine which shipments to display for the current page
    start_index = (current_page - 1) * shipments_per_page
    end_index = min(current_page * shipments_per_page, len(shipments))
    page_shipments = shipments[start_index:end_index]

    # Create a response for the current page of shipments
    response = "📋 All Shipments:\n"
    for shipment in page_shipments:
        response += (
            f"📦 Shipment ID: {shipment.get('Shipment ID', 'N/A')}\n"
            f"👤 Customer: {shipment.get('Customer Name', 'N/A')}\n"
            f"🏠 Address: {shipment.get('Address', 'N/A')}\n"
            f"📮 Tracking Number: {shipment.get('Tracking Number', 'N/A')}\n"
            f"📷 Photos: {shipment.get('Photos', 'N/A')}\n"
            f"📅 Created At: {shipment['created_at']}\n"
            f"🔄 Updated At: {shipment['updated_at']}\n\n"
        )

    # Add pagination controls (Next/Previous)
    pagination_controls = ""
    if current_page > 1:
        pagination_controls += "/previous - Previous Page\n"
    if current_page < total_pages:
        pagination_controls += "/next - Next Page"

    await update.message.reply_text(response + pagination_controls)

async def handle_view_by_id(update, context):
    """Prompt user to enter the shipment ID"""
    await update.message.reply_text("🔍 Please enter the shipment ID:")
    return VIEW_BY_ID  # Change to VIEW_BY_ID state

async def handle_shipment_id(update, context):
    """Process the shipment ID entered by the user"""
    shipment_id = update.message.text.strip()

    # If the user enters a command or empty text, return early
    if update.message.text.startswith("/") or not shipment_id:
        await update.message.reply_text("❌ Please enter a valid shipment ID.")
        return VIEW_BY_ID  # Stay in the VIEW_BY_ID state

    # Look up the shipment in the database
    shipment = db.get_shipment(shipment_id)
    
    if shipment:
        response = (
            f"📦 Shipment ID: {shipment[0]}\n"
            f"👤 Customer: {shipment[1]}\n"
            f"🏠 Address: {shipment[2]}\n"
            f"📮 Tracking Number: {shipment[3]}\n"
            f"📷 Photos: {shipment[4]}\n"
            f"📅 Created At: {shipment[6]}\n"
            f"🔄 Updated At: {shipment[7]}"
        )
    else:
        response = "❌ Shipment not found"
    
    await update.message.reply_text(response)
    return ConversationHandler.END  # End the conversation after processing the shipment ID

async def handle_previous_page(update, context):
    """Go to the previous page"""
    current_page = context.user_data.get('current_page', 1)
    current_page = max(1, current_page - 1)  # Ensure page does not go below 1
    context.user_data['current_page'] = current_page

    # Call the `handle_view_all` function again to show the previous page of results
    await handle_view_all(update, context)

async def handle_next_page(update, context):
    """Go to the next page"""
    current_page = context.user_data.get('current_page', 1)
    current_page += 1
    context.user_data['current_page'] = current_page

    # Call the `handle_view_all` function again to show the next page of results
    await handle_view_all(update, context)

def setup_view_handlers(app):
    """Set up the handler for viewing a shipment by ID"""
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex(r"^🔍 View by ID$"), handle_view_by_id)],
        states={
            VIEW_BY_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_shipment_id)],  # Handle shipment ID input
        },
        fallbacks=[]  # No fallbacks, only proceed with ID viewing
    )
    app.add_handler(conv_handler)

    # Regular handlers for viewing all shipments and pagination
    app.add_handler(MessageHandler(filters.Regex(r"^📋 View All Shipments$"), handle_view_all))
    app.add_handler(CommandHandler("next", handle_next_page))  # Handler for next page
    app.add_handler(CommandHandler("previous", handle_previous_page))  # Handler for previous page
