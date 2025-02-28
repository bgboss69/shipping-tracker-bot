    # # import os
    # # from dotenv import load_dotenv
    # # from telegram import Update, ReplyKeyboardMarkup
    # # from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext
    # # from telegram.ext import filters  

    # # # 加载环境变量
    # # load_dotenv()

    # # # 初始化数据库
    # # from database import Database
    # # db = Database()

    # # async def start(update: Update, context: CallbackContext):
    # #     buttons = [
    # #         ["📦 New Shipment"],
    # #         ["📋 View All Shipments"],
    # #         ["🔍 View by ID"],
    # #         ["🆘 Help"]
    # #     ]
    # #     await update.message.reply_text(
    # #         "Main Menu:",
    # #         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    # #     )

    # # async def handle_new_shipment(update: Update, context: CallbackContext):
    # #     # 这里添加收集信息的逻辑
    # #     await update.message.reply_text("Please enter customer name:")

    # # def main():
    # #     # Initialize the application with the bot token
    # #     application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

    # #     # Add command handler for "/start"
    # #     application.add_handler(CommandHandler("start", start))

    # #     # Add message handler for the "New Shipment" button
    # #     application.add_handler(MessageHandler(filters.Regex('^📦 New Shipment$'), handle_new_shipment))

    # #     # Start polling for updates
    # #     application.run_polling()

    # # if __name__ == '__main__':
    # #     main()

    # # import os
    # # from dotenv import load_dotenv
    # # from telegram import Update, ReplyKeyboardMarkup
    # # from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
    # # from telegram.ext import filters

    # # # 加载环境变量
    # # load_dotenv()

    # # # 初始化数据库
    # # from database import Database
    # # db = Database()

    # # # 记录当前状态的字典，用于跟踪用户输入的进度
    # # user_data = {}

    # # async def start(update: Update, context: CallbackContext):
    # #     buttons = [
    # #         ["📦 New Shipment"],
    # #         ["📋 View All Shipments"],
    # #         ["🔍 View by ID"],
    # #         ["🆘 Help"]
    # #     ]
    # #     await update.message.reply_text(
    # #         "Main Menu:",
    # #         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    # #     )

    # # async def handle_new_shipment(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id] = {}
    # #     await update.message.reply_text("Please enter customer name:")

    # # async def handle_customer_name(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['customer_name'] = update.message.text
    # #     await update.message.reply_text("Please enter the address:")

    # # async def handle_address(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['address'] = update.message.text
    # #     await update.message.reply_text("Please enter the tracking number:")

    # # async def handle_tracking_number(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['tracking_number'] = update.message.text
    # #     await update.message.reply_text("Please enter the photos (comma-separated URLs):")

    # # async def handle_photos(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['photos'] = update.message.text.split(',')
    # #     # Create shipment and store it in Google Sheets
    # #     shipment_id = db.create_shipment(user_data[update.message.chat.id])
    # #     await update.message.reply_text(f"Shipment created successfully! Shipment ID: {shipment_id}")
    # #     # Clear the user's data after creation
    # #     del user_data[update.message.chat.id]
    # #     await start(update, context)

    # # async def handle_view_all_shipments(update: Update, context: CallbackContext):
    # #     # Get all shipments from the sheet
    # #     records = db.sheet.get_all_records()
    # #     if not records:
    # #         await update.message.reply_text("No shipments found.")
    # #     else:
    # #         # Display shipments as a list
    # #         message = "All Shipments:\n"
    # #         for record in records:
    # #             message += f"ID: {record['Shipment ID']}, Customer: {record['Customer Name']}, Status: {record['Status']}\n"
    # #         await update.message.reply_text(message)

    # # async def handle_view_by_id(update: Update, context: CallbackContext):
    # #     await update.message.reply_text("Please enter the Shipment ID:")

    # # async def handle_shipment_id(update: Update, context: CallbackContext):
    # #     shipment_id = update.message.text
    # #     # Search for the shipment by ID
    # #     records = db.sheet.get_all_records()
    # #     shipment = next((r for r in records if r['Shipment ID'] == shipment_id), None)
    # #     if shipment:
    # #         message = f"Shipment ID: {shipment['Shipment ID']}\n"
    # #         message += f"Customer: {shipment['Customer Name']}\n"
    # #         message += f"Address: {shipment['Address']}\n"
    # #         message += f"Tracking Number: {shipment['Tracking Number']}\n"
    # #         message += f"Status: {shipment['Status']}\n"
    # #         message += f"Photos: {shipment['Photos']}\n"
    # #         await update.message.reply_text(message)
    # #     else:
    # #         await update.message.reply_text("Shipment not found.")

    # # async def handle_help(update: Update, context: CallbackContext):
    # #     help_message = (
    # #         "Welcome to the Shipment Management Bot!\n"
    # #         "Here's how you can use the bot:\n"
    # #         "1. 📦 New Shipment: Create a new shipment record.\n"
    # #         "2. 📋 View All Shipments: View all shipments.\n"
    # #         "3. 🔍 View by ID: Look up a shipment by its ID.\n"
    # #         "4. 🆘 Help: Get help information about using the bot."
    # #     )
    # #     await update.message.reply_text(help_message)

    # # def main():
    # #     # Initialize the application with the bot token
    # #     application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

    # #     # Add command handler for "/start"
    # #     application.add_handler(CommandHandler("start", start))

    # #     # Add message handler for the "New Shipment" button
    # #     application.add_handler(MessageHandler(filters.Regex('^📦 New Shipment$'), handle_new_shipment))

    # #     # Add handlers for collecting shipment information
    # #     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_customer_name))
    # #     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address))
    # #     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tracking_number))
    # #     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_photos))


    # #     # Add message handlers for other options
    # #     application.add_handler(MessageHandler(filters.Regex('^📋 View All Shipments$'), handle_view_all_shipments))
    # #     application.add_handler(MessageHandler(filters.Regex('^🔍 View by ID$'), handle_view_by_id))
    # #     application.add_handler(MessageHandler(filters.Regex('^🆘 Help$'), handle_help))

    # #     # Start polling for updates
    # #     application.run_polling()

    # # if __name__ == '__main__':
    # #     main()

    # ###

    # # import os
    # # from dotenv import load_dotenv
    # # from telegram import Update, ReplyKeyboardMarkup
    # # from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, ConversationHandler
    # # from telegram.ext import filters
    # # from database import Database

    # # # Load environment variables
    # # load_dotenv()

    # # # Initialize database
    # # db = Database()

    # # # Define states for conversation
    # # CUSTOMER_NAME, ADDRESS, TRACKING_NUMBER, PHOTOS = range(4)

    # # # Create a dictionary to store user data during the conversation
    # # user_data = {}

    # # # Start the bot
    # # async def start(update: Update, context: CallbackContext):
    # #     buttons = [
    # #         ["📦 New Shipment"],
    # #         ["📋 View All Shipments"],
    # #         ["🔍 View by ID"],
    # #         ["🆘 Help"]
    # #     ]
    # #     await update.message.reply_text(
    # #         "Main Menu:",
    # #         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    # #     )

    # # # Start the "New Shipment" process
    # # async def handle_new_shipment(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id] = {}  # Initialize user data for this conversation
    # #     await update.message.reply_text("Please enter customer name:")
    # #     return CUSTOMER_NAME

    # # # Handle customer name input
    # # async def handle_customer_name(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['customer_name'] = update.message.text
    # #     await update.message.reply_text("Please enter the address:")
    # #     return ADDRESS

    # # # Handle address input
    # # async def handle_address(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['address'] = update.message.text
    # #     await update.message.reply_text("Please enter the tracking number:")
    # #     return TRACKING_NUMBER

    # # # Handle tracking number input
    # # async def handle_tracking_number(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['tracking_number'] = update.message.text
    # #     await update.message.reply_text("Please enter the photos (comma-separated URLs):")
    # #     return PHOTOS

    # # # Handle photos input
    # # async def handle_photos(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id]['photos'] = update.message.text.split(',')
        
    # #     # Create shipment and store it in Google Sheets
    # #     shipment_id = db.create_shipment(user_data[update.message.chat.id])
    # #     await update.message.reply_text(f"Shipment created successfully! Shipment ID: {shipment_id}")
        
    # #     # Clear the user's data after creation
    # #     del user_data[update.message.chat.id]
    # #     await start(update, context)
    # #     return ConversationHandler.END

    # # # Handle viewing all shipments
    # # async def handle_view_all_shipments(update: Update, context: CallbackContext):
    # #     records = db.sheet.get_all_records()
    # #     if not records:
    # #         await update.message.reply_text("No shipments found.")
    # #     else:
    # #         message = "All Shipments:\n"
    # #         for record in records:
    # #             message += f"ID: {record['Shipment ID']}, Customer: {record['Customer Name']}, Status: {record['Status']}\n"
    # #         await update.message.reply_text(message)

    # # # Handle viewing a shipment by ID
    # # async def handle_view_by_id(update: Update, context: CallbackContext):
    # #     await update.message.reply_text("Please enter the Shipment ID:")

    # # # Handle viewing shipment details by ID
    # # async def handle_shipment_id(update: Update, context: CallbackContext):
    # #     shipment_id = update.message.text
    # #     records = db.sheet.get_all_records()
    # #     shipment = next((r for r in records if r['Shipment ID'] == shipment_id), None)
    # #     if shipment:
    # #         message = f"Shipment ID: {shipment['Shipment ID']}\n"
    # #         message += f"Customer: {shipment['Customer Name']}\n"
    # #         message += f"Address: {shipment['Address']}\n"
    # #         message += f"Tracking Number: {shipment['Tracking Number']}\n"
    # #         message += f"Status: {shipment['Status']}\n"
    # #         message += f"Photos: {shipment['Photos']}\n"
    # #         await update.message.reply_text(message)
    # #     else:
    # #         await update.message.reply_text("Shipment not found.")

    # # # Handle help command
    # # async def handle_help(update: Update, context: CallbackContext):
    # #     help_message = (
    # #         "Welcome to the Shipment Management Bot!\n"
    # #         "Here's how you can use the bot:\n"
    # #         "1. 📦 New Shipment: Create a new shipment record.\n"
    # #         "2. 📋 View All Shipments: View all shipments.\n"
    # #         "3. 🔍 View by ID: Look up a shipment by its ID.\n"
    # #         "4. 🆘 Help: Get help information about using the bot."
    # #     )
    # #     await update.message.reply_text(help_message)

    # # # Cancel the conversation if needed
    # # async def cancel(update: Update, context: CallbackContext):
    # #     await update.message.reply_text("The process has been canceled.")
    # #     return ConversationHandler.END

    # # def main():
    # #     # Initialize the application with the bot token
    # #     application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

    # #     # Define the conversation handler
    # #     conversation_handler = ConversationHandler(
    # #         entry_points=[MessageHandler(filters.Regex('^📦 New Shipment$'), handle_new_shipment)],
    # #         states={
    # #             CUSTOMER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_customer_name)],
    # #             ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address)],
    # #             TRACKING_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tracking_number)],
    # #             PHOTOS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_photos)],
    # #         },
    # #         fallbacks=[CommandHandler('cancel', cancel)]  # Allow the user to cancel anytime
    # #     )

    # #     # Add handlers
    # #     application.add_handler(conversation_handler)

    # #     # Add message handlers for other options
    # #     application.add_handler(MessageHandler(filters.Regex('^📋 View All Shipments$'), handle_view_all_shipments))
    # #     application.add_handler(MessageHandler(filters.Regex('^🔍 View by ID$'), handle_view_by_id))
    # #     application.add_handler(MessageHandler(filters.Regex('^🆘 Help$'), handle_help))

    # #     # Start polling for updates
    # #     application.run_polling()

    # # if __name__ == '__main__':
    # #     main()

    # ###
    # import os
    # from dotenv import load_dotenv
    # from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
    # from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, ConversationHandler
    # from telegram.ext import filters
    # from database import Database
    # from io import BytesIO
    # from googleapiclient.discovery import build
    # from googleapiclient.http import MediaIoBaseUpload
    # from google.oauth2 import service_account

    # # Load environment variables
    # load_dotenv()

    # # Initialize database
    # db = Database()

    # # Define states for conversation
    # CUSTOMER_NAME, ADDRESS, TRACKING_NUMBER, PHOTOS = range(4)

    # # Create a dictionary to store user data during the conversation
    # user_data = {}

    # # Start the bot
    # async def start(update: Update, context: CallbackContext):
    #     buttons = [
    #         ["📦 New Shipment"],
    #         ["📋 View All Shipments"],
    #         ["🔍 View by ID"],
    #         ["🆘 Help"]
    #     ]
    #     await update.message.reply_text(
    #         "Main Menu:",
    #         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    #     )

    # # # Start the "New Shipment" process
    # # async def handle_new_shipment(update: Update, context: CallbackContext):
    # #     user_data[update.message.chat.id] = {}  # Initialize user data for this conversation
    # #     await update.message.reply_text("Please enter customer name:")
    # #     return CUSTOMER_NAME
    # async def handle_new_shipment(update: Update, context: CallbackContext):
    #     # Initialize user data for this conversation
    #     user_data[update.message.chat.id] = {}
        
    #     # Generate the shipment ID by creating a new shipment in the database
    #     shipment_data = {
    #         'customer_name': '',  # You will populate these fields during the conversation
    #         'address': '',
    #         'tracking_number': '',
    #         'photos': []  # Empty initially, will be filled later
    #     }
        
    #     # Generate shipment ID and store it in user_data
    #     shipment_id = db.create_shipment(shipment_data)
    #     user_data[update.message.chat.id]['shipment_id'] = shipment_id  # Store the shipment ID
        
    #     await update.message.reply_text("Please enter customer name:")
    #     return CUSTOMER_NAME


    # # Handle customer name input
    # async def handle_customer_name(update: Update, context: CallbackContext):
    #     user_data[update.message.chat.id]['customer_name'] = update.message.text
    #     await update.message.reply_text("Please enter the address:")
    #     return ADDRESS

    # # Handle address input
    # async def handle_address(update: Update, context: CallbackContext):
    #     user_data[update.message.chat.id]['address'] = update.message.text
    #     await update.message.reply_text("Please enter the tracking number:")
    #     return TRACKING_NUMBER

    # # Handle tracking number input
    # async def handle_tracking_number(update: Update, context: CallbackContext):
    #     user_data[update.message.chat.id]['tracking_number'] = update.message.text
    #     await update.message.reply_text("Please upload the photos (optional):\nYou can send one or skip this step by typing 'skip'.")
    #     return PHOTOS

    # # Function to upload the file directly from memory
    # def upload_file_to_drive_from_memory(file_bytes, shipment_id, mime_type='image/jpeg'):
    #     creds = service_account.Credentials.from_service_account_file(
    #         'credentials.json', scopes=['https://www.googleapis.com/auth/drive.file']
    #     )

    #     service = build('drive', 'v3', credentials=creds)
        
    #     # Set the file name to the shipment ID with the .jpg extension
    #     file_name = f'{shipment_id}.jpg'
        
    #     # Upload the file to Google Drive
    #     media = MediaIoBaseUpload(BytesIO(file_bytes), mimetype=mime_type)
    #     file_metadata = {'name': file_name}  # Dynamic file name based on shipment ID
    #     file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
    #     # Get the file ID and generate the public URL to access the file
    #     file_id = file.get('id')
    #     file_url = f'https://drive.google.com/uc?id={file_id}'
        
    #     return file_url

    # # Function to insert the image into Google Sheets
    # def insert_image_into_sheet(spreadsheet_id, sheet_name, cell, image_url):
    #     creds = service_account.Credentials.from_service_account_file(
    #         'credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets']
    #     )
    #     service = build('sheets', 'v4', credentials=creds)
        
    #     # Construct the formula to insert the image
    #     image_formula = f'IMAGE("{image_url}")'

    #     # Update the cell with the image formula
    #     request = service.spreadsheets().values().update(
    #         spreadsheetId=spreadsheet_id,
    #         range=f'{sheet_name}!{cell}',
    #         valueInputOption='RAW',
    #         body={'values': [[image_formula]]}
    #     ).execute()

    #     print(f'Image inserted into {sheet_name}!{cell}')

    # # Handle photos input
    # async def handle_photos(update: Update, context: CallbackContext):
    #     chat_id = update.message.chat.id

    #     # Retrieve the shipment_id from user_data (this was set earlier during shipment creation)
    #     shipment_id = user_data[chat_id].get('shipment_id', 'Unknown')  # Retrieve the shipment ID
        
    #     if update.message.photo:
    #         # Get the highest resolution photo
    #         photo = update.message.photo[-1]
    #         file_id = photo.file_id
            
    #         # Get the file object from Telegram API
    #         file = await context.bot.get_file(file_id)
            
    #         # Download the file directly to memory (instead of the file system)
    #         photo_bytes = await file.download_as_bytearray()
            
    #         # Upload the photo to Google Drive
    #         file_url = upload_file_to_drive_from_memory(photo_bytes, shipment_id)
            
    #         # Insert the image into Google Sheets
    #         spreadsheet_id = 'your-google-sheet-id'  # The ID of your Google Sheets
    #         sheet_name = 'Sheet1'  # The name of your sheet
            
    #         # Find the row containing the shipment_id and get its row index
    #         row_index = db.find_shipment_row_by_id(shipment_id)
            
    #         if row_index:
    #             # Update the "Photos" column (assuming it's the 7th column)
    #             cell = f'G{row_index}'  # Column G (7th column) for Photos
    #             insert_image_into_sheet(spreadsheet_id, sheet_name, cell, file_url)
                
    #             # Save the photo's URL in user_data
    #             user_data[chat_id]['photos'] = [file_url]

    #             # Update the shipment record with the photo URL in the database
    #             db.update_shipment_photos(shipment_id, [file_url])
                
    #             await update.message.reply_text(f"Photo uploaded and inserted into Google Sheets successfully. You can type 'skip' if you want to skip other steps.")
    #         else:
    #             await update.message.reply_text(f"Shipment ID {shipment_id} not found in the database.")
    #     elif update.message.text.lower() == 'skip':
    #         user_data[chat_id]['photos'] = []  # No photos uploaded
    #         await update.message.reply_text("No photo uploaded. Proceeding to the next step.")
    #     else:
    #         # Invalid input, ask for photos again
    #         await update.message.reply_text("Please upload a photo or type 'skip' to skip this step.")
    #         return PHOTOS  # Stay at the same step

    #     # Once photos are handled, proceed to create shipment
    #     await handle_shipment_creation(update, context)
    #     return ConversationHandler.END

    # # Create shipment and store it in the database
    # async def handle_shipment_creation(update: Update, context: CallbackContext):
    #     shipment_id = db.create_shipment(user_data[update.message.chat.id])
    #     await update.message.reply_text(f"Shipment created successfully! Shipment ID: {shipment_id}")
        
    #     # Clear the user's data after creation
    #     del user_data[update.message.chat.id]
    #     await start(update, context)

    # # Handle viewing all shipments
    # async def handle_view_all_shipments(update: Update, context: CallbackContext):
    #     records = db.sheet.get_all_records()  # Fetch all records from Google Sheets
    #     if not records:
    #         await update.message.reply_text("No shipments found.")
    #     else:
    #         message = "All Shipments:\n"
    #         for record in records:
    #             # Safely access 'Shipment ID' and other keys
    #             shipment_id = record.get('Shipment ID', 'N/A')
    #             customer_name = record.get('Customer Name', 'Unknown')
    #             status = record.get('Status', 'N/A')
                
    #             message += f"ID: {shipment_id}, Customer: {customer_name}, Status: {status}\n"
            
    #         await update.message.reply_text(message)

    # # Handle viewing a shipment by ID
    # async def handle_view_by_id(update: Update, context: CallbackContext):
    #     await update.message.reply_text("Please enter the Shipment ID:")

    # # Handle viewing shipment details by ID
    # async def handle_shipment_id(update: Update, context: CallbackContext):
    #     shipment_id = update.message.text
    #     records = db.sheet.get_all_records()
    #     shipment = next((r for r in records if r['Shipment ID'] == shipment_id), None)
    #     if shipment:
    #         message = f"Shipment ID: {shipment['Shipment ID']}\n"
    #         message += f"Customer: {shipment['Customer Name']}\n"
    #         message += f"Address: {shipment['Address']}\n"
    #         message += f"Tracking Number: {shipment['Tracking Number']}\n"
    #         message += f"Status: {shipment['Status']}\n"
    #         message += f"Photos: {shipment['Photos']}\n"
    #         await update.message.reply_text(message)
    #     else:
    #         await update.message.reply_text("Shipment not found.")

    # # Handle help command
    # async def handle_help(update: Update, context: CallbackContext):
    #     help_message = (
    #         "Welcome to the Shipment Management Bot!\n"
    #         "Here's how you can use the bot:\n"
    #         "1. 📦 New Shipment: Create a new shipment record.\n"
    #         "2. 📋 View All Shipments: View all shipments.\n"
    #         "3. 🔍 View by ID: Look up a shipment by its ID.\n"
    #         "4. 🆘 Help: Get help information about using the bot."
    #     )
    #     await update.message.reply_text(help_message)

    # # Cancel the conversation if needed
    # async def cancel(update: Update, context: CallbackContext):
    #     await update.message.reply_text("The process has been canceled.")
    #     return ConversationHandler.END

    # # Handler for user corrections (retrying or going back)
    # async def handle_retry(update: Update, context: CallbackContext):
    #     await update.message.reply_text("You can go back and correct your previous inputs by typing 'retry'.")
    #     # Reset to the previous step (if necessary) based on the current state
    #     return ConversationHandler.END

    # def main():
    #     # Initialize the application with the bot token
    #     application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

    #     # Define the conversation handler
    #     conversation_handler = ConversationHandler(
    #         entry_points=[MessageHandler(filters.Regex('^📦 New Shipment$'), handle_new_shipment)],
    #         states={
    #             CUSTOMER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_customer_name)],
    #             ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address)],
    #             TRACKING_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tracking_number)],
    #             PHOTOS: [MessageHandler(filters.PHOTO | filters.TEXT, handle_photos)],  # Handle both photo uploads and text inputs (skip)
    #         },
    #         fallbacks=[CommandHandler('cancel', cancel), MessageHandler(filters.TEXT & ~filters.COMMAND, handle_retry)]  # Retry handling
    #     )

    #     # Add handlers
    #     application.add_handler(conversation_handler)

    #     # Add message handlers for other options
    #     application.add_handler(MessageHandler(filters.Regex('^📋 View All Shipments$'), handle_view_all_shipments))
    #     application.add_handler(MessageHandler(filters.Regex('^🔍 View by ID$'), handle_view_by_id))
    #     application.add_handler(MessageHandler(filters.Regex('^🆘 Help$'), handle_help))

    #     # Start polling for updates
    #     application.run_polling()

    # if __name__ == '__main__':
    #     main()




    # # # Handle photos input
    # # async def handle_photos(update: Update, context: CallbackContext):
    #     # chat_id = update.message.chat.id
        
    #     # # Check if the user uploaded a photo or typed 'skip'
    #     # if update.message.photo:
    #     #     # Get the highest resolution photo
    #     #     photo = update.message.photo[-1]
    #     #     file_id = photo.file_id
            
    #     #     # Get the file object from Telegram API
    #     #     file = await context.bot.get_file(file_id)
    #     #     file_url = file.file_path  # This will give you the URL to access the file

    #     #     # Download the file to the local file system (provide a full path if needed)
    #     #     await file.download_to_drive(f"{chat_id}_photo.jpg")  # Save the file locally
            
    #     #     # Save the photo's file_id in user_data
    #     #     user_data[chat_id]['photos'] = [file_id]
    #     #     await update.message.reply_text("Photo uploaded successfully. You can type 'skip' if you want to skip other steps.")
    #     # elif update.message.text.lower() == 'skip':
    #     #     user_data[chat_id]['photos'] = []  # No photos uploaded
    #     #     await update.message.reply_text("No photo uploaded. Proceeding to the next step.")
    #     # else:
    #     #     # Invalid input, ask for photos again
    #     #     await update.message.reply_text("Please upload a photo or type 'skip' to skip this step.")
    #     #     return PHOTOS  # Stay at the same step

    #     # # Once photos are handled, proceed to create shipment
    #     # await handle_shipment_creation(update, context)
    #     # return ConversationHandler.END


    # # async def handle_photos(update: Update, context: CallbackContext):
    # #     chat_id = update.message.chat.id
        
    # #     # Check if the user uploaded a photo or typed 'skip'
    # #     if update.message.photo:
    # #         # Get the highest resolution photo
    # #         photo = update.message.photo[-1]
    # #         file_id = photo.file_id
            
    # #         # Get the file object from Telegram API
    # #         file = await context.bot.get_file(file_id)
            
    # #         # Download the file directly to memory (instead of the file system)
    # #         photo_bytes = await file.download_as_bytearray()
            
    # #         # Upload the photo to Google Drive
    # #         file_url = upload_file_to_drive_from_memory(photo_bytes)
            
    # #         # Save the photo's URL in user_data
    # #         user_data[chat_id]['photos'] = [file_url]
    # #         await update.message.reply_text(f"Photo uploaded successfully! You can type 'skip' if you want to skip other steps.")
    # #     elif update.message.text.lower() == 'skip':
    # #         user_data[chat_id]['photos'] = []  # No photos uploaded
    # #         await update.message.reply_text("No photo uploaded. Proceeding to the next step.")
    # #     else:
    # #         # Invalid input, ask for photos again
    # #         await update.message.reply_text("Please upload a photo or type 'skip' to skip this step.")
    # #         return PHOTOS  # Stay at the same step

    # #     # Once photos are handled, proceed to create shipment
    # #     await handle_shipment_creation(update, context)
    # #     return ConversationHandler.END

    # # # Function to upload the file directly from memory
    # # def upload_file_to_drive_from_memory(file_bytes, mime_type='image/jpeg'):
    # #     creds = service_account.Credentials.from_service_account_file(
    # #         'path/to/your/credentials.json', scopes=['https://www.googleapis.com/auth/drive.file']
    # #     )
    # #     service = build('drive', 'v3', credentials=creds)
        
    # #     file_metadata = {'name': 'photo.jpg'}
    # #     media = MediaIoBaseUpload(BytesIO(file_bytes), mimetype=mime_type)
        
    # #     file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
    # #     file_id = file.get('id')
    # #     file_url = f'https://drive.google.com/uc?id={file_id}'
        
    # #     return file_url

    import os
    from dotenv import load_dotenv
    from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
    from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, ConversationHandler
    from telegram.ext import filters
    from database import Database
    from io import BytesIO
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseUpload
    from google.oauth2 import service_account

    # Load environment variables
    load_dotenv()

    # Initialize database
    db = Database()

    # Define states for conversation
    CUSTOMER_NAME, ADDRESS, TRACKING_NUMBER, PHOTOS = range(4)

    # Create a dictionary to store user data during the conversation
    user_data = {}

    # Start the bot
    async def start(update: Update, context: CallbackContext):
        buttons = [
            ["📦 New Shipment"],
            ["📋 View All Shipments"],
            ["🔍 View by ID"],
            ["🆘 Help"]
        ]
        await update.message.reply_text(
            "Main Menu:",
            reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        )

    async def handle_shipment_creation(update: Update, context: CallbackContext):
        chat_id = update.message.chat.id
        shipment_id = user_data[chat_id].get('shipment_id', 'Unknown')
        
        # Your logic for creating the shipment goes here
        await update.message.reply_text(f"Shipment {shipment_id} created successfully!")


    # Start the "New Shipment" process
    async def handle_new_shipment(update: Update, context: CallbackContext):
        user_data[update.message.chat.id] = {}  # Initialize user data for this conversation
        
        # Generate shipment ID and store it in user_data
        shipment_data = {
            'customer_name': '',
            'address': '',
            'tracking_number': '',
            'photos': []  # Empty initially, will be filled later
        }
        
        shipment_id = db.create_shipment(shipment_data)  # Create shipment in the DB
        user_data[update.message.chat.id]['shipment_id'] = shipment_id  # Store shipment ID
        
        await update.message.reply_text("Please enter customer name:")
        return CUSTOMER_NAME

    # Handle customer name input
    async def handle_customer_name(update: Update, context: CallbackContext):
        user_data[update.message.chat.id]['customer_name'] = update.message.text
        await update.message.reply_text("Please enter the address:")
        return ADDRESS

    # Handle address input
    async def handle_address(update: Update, context: CallbackContext):
        user_data[update.message.chat.id]['address'] = update.message.text
        await update.message.reply_text("Please enter the tracking number:")
        return TRACKING_NUMBER

    # Handle tracking number input
    async def handle_tracking_number(update: Update, context: CallbackContext):
        user_data[update.message.chat.id]['tracking_number'] = update.message.text
        await update.message.reply_text("Please upload the photos (optional):\nYou can send one or skip this step by typing 'skip'.")
        return PHOTOS
        
    # Function to upload the file directly from memory
    def upload_file_to_drive_from_memory(file_bytes, shipment_id, mime_type='image/jpeg'):
        creds = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=['https://www.googleapis.com/auth/drive.file']
        )

        service = build('drive', 'v3', credentials=creds)
        
        # Set the file name to the shipment ID with the .jpg extension
        file_name = f'{shipment_id}.jpg'
        
        # Upload the file to Google Drive
        media = MediaIoBaseUpload(BytesIO(file_bytes), mimetype=mime_type)
        file_metadata = {'name': file_name}  # Dynamic file name based on shipment ID
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        
        # Get the file ID and generate the public URL to access the file
        file_id = file.get('id')
        file_url = f'https://drive.google.com/uc?id={file_id}'
        
        return file_url

    # Function to insert the image into Google Sheets
    def insert_image_into_sheet(spreadsheet_id, sheet_name, cell, image_url):
        creds = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        service = build('sheets', 'v4', credentials=creds)
        
        # Construct the formula to insert the image
        image_formula = f'IMAGE("{image_url}")'

        # Update the cell with the image formula
        request = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f'{sheet_name}!{cell}',
            valueInputOption='RAW',
            body={'values': [[image_formula]]}
        ).execute()

        print(f'Image inserted into {sheet_name}!{cell}')

    # # Handle photos input
    # async def handle_photos(update: Update, context: CallbackContext):
    #     chat_id = update.message.chat.id
    #     shipment_id = user_data[chat_id].get('shipment_id', 'Unknown')  # Retrieve the shipment ID
        
    #     if update.message.photo:
    #         # Get the highest resolution photo
    #         photo = update.message.photo[-1]
    #         file_id = photo.file_id
            
    #         # Get the file object from Telegram API
    #         file = await context.bot.get_file(file_id)
            
    #         # Download the file directly to memory (instead of the file system)
    #         photo_bytes = await file.download_as_bytearray()
            
    #         # Upload the photo to Google Drive
    #         file_url = upload_file_to_drive_from_memory(photo_bytes, shipment_id)
            
    #         # Retrieve the spreadsheet_id and sheet_name from the Database class
    #         spreadsheet_id = db.get_spreadsheet_id()  # From database
    #         sheet_name = db.get_sheet_name()  # From database
            
    #         # Find the row containing the shipment_id and get its row index
    #         row_index = db.find_shipment_row_by_id(shipment_id)
            
    #         if row_index:
    #             # Update the "Photos" column (assuming it's the 7th column)
    #             cell = f'G{row_index}'  # Column G (7th column) for Photos
    #             insert_image_into_sheet(spreadsheet_id, sheet_name, cell, file_url)
                
    #             # Save the photo's URL in user_data
    #             user_data[chat_id]['photos'] = [file_url]

    #             # Update the shipment record with the photo URL in the database
    #             db.update_shipment_photos(shipment_id, [file_url])
                
    #             await update.message.reply_text(f"Photo uploaded and inserted into Google Sheets successfully. You can type 'skip' if you want to skip other steps.")
    #         else:
    #             await update.message.reply_text(f"Shipment ID {shipment_id} not found in the database.")
    #     elif update.message.text.lower() == 'skip':
    #         user_data[chat_id]['photos'] = []  # No photos uploaded
    #         await update.message.reply_text("No photo uploaded. Proceeding to the next step.")
    #     else:
    #         # Invalid input, ask for photos again
    #         await update.message.reply_text("Please upload a photo or type 'skip' to skip this step.")
    #         return PHOTOS  # Stay at the same step

    #     # Once photos are handled, proceed to create shipment
    #     await handle_shipment_creation(update, context)
    #     return ConversationHandler.END
    async def handle_photos(update: Update, context: CallbackContext):
        chat_id = update.message.chat.id
        shipment_id = user_data[chat_id].get('shipment_id', 'Unknown')  # Retrieve the shipment ID
        
        if update.message.photo:
            # Get the highest resolution photo
            photo = update.message.photo[-1]
            file_id = photo.file_id
            
            # Get the file object from Telegram API
            file = await context.bot.get_file(file_id)
            
            # Download the file directly to memory (instead of the file system)
            photo_bytes = await file.download_as_bytearray()
            
            # Upload the photo to Google Drive
            file_url = upload_file_to_drive_from_memory(photo_bytes, shipment_id)
            
            # Retrieve the spreadsheet_id and sheet_name from the Database class
            spreadsheet_id = db.get_spreadsheet_id()  # From database
            sheet_name = db.get_sheet_name()  # From database
            
            # Find the row containing the shipment_id directly
            records = db.sheet.get_all_records()
            shipment = next((record for record in records if record['Shipment ID'] == shipment_id), None)
            
            if shipment:
                row_index = records.index(shipment) + 2  # +2 because get_all_records returns a 0-indexed list, and rows start at 2 in Google Sheets
                
                # Update the "Photos" column (assuming it's the 7th column)
                cell = f'G{row_index}'  # Column G (7th column) for Photos
                insert_image_into_sheet(spreadsheet_id, sheet_name, cell, file_url)
                
                # Save the photo's URL in user_data
                user_data[chat_id]['photos'] = [file_url]

                # Update the shipment record with the photo URL in the database
                db.update_shipment_photos(shipment_id, [file_url])
                
                await update.message.reply_text(f"Photo uploaded and inserted into Google Sheets successfully. You can type 'skip' if you want to skip other steps.")
            else:
                await update.message.reply_text(f"Shipment ID {shipment_id} not found in the database.")
        elif update.message.text.lower() == 'skip':
            user_data[chat_id]['photos'] = []  # No photos uploaded
            await update.message.reply_text("No photo uploaded. Proceeding to the next step.")
        else:
            # Invalid input, ask for photos again
            await update.message.reply_text("Please upload a photo or type 'skip' to skip this step.")
            return PHOTOS  # Stay at the same step

        # Once photos are handled, proceed to create shipment
        await handle_shipment_creation(update, context)
        return ConversationHandler.END

    # Handle viewing all shipments
    async def handle_view_all_shipments(update: Update, context: CallbackContext):
        # Assuming that db.sheet.get_all_records() will retrieve the list of all shipments
        records = db.sheet.get_all_records()  # Fetch all records from Google Sheets
        if not records:
            await update.message.reply_text("No shipments found.")
        else:
            message = "All Shipments:\n"
            for record in records:
                # Safely access 'Shipment ID' and other keys
                shipment_id = record.get('Shipment ID', 'N/A')
                customer_name = record.get('Customer Name', 'Unknown')
                status = record.get('Status', 'N/A')
                
                message += f"ID: {shipment_id}, Customer: {customer_name}, Status: {status}\n"
            
            await update.message.reply_text(message)

    # Handle viewing a shipment by ID
    async def handle_view_by_id(update: Update, context: CallbackContext):
        await update.message.reply_text("Please enter the Shipment ID:")

    # Handle viewing shipment details by ID
    async def handle_shipment_id(update: Update, context: CallbackContext):
        shipment_id = update.message.text
        records = db.sheet.get_all_records()
        shipment = next((r for r in records if r['Shipment ID'] == shipment_id), None)
        if shipment:
            message = f"Shipment ID: {shipment['Shipment ID']}\n"
            message += f"Customer: {shipment['Customer Name']}\n"
            message += f"Address: {shipment['Address']}\n"
            message += f"Tracking Number: {shipment['Tracking Number']}\n"
            message += f"Status: {shipment['Status']}\n"
            message += f"Photos: {shipment['Photos']}\n"
            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Shipment not found.")

    # Handler for user corrections (retrying or going back)
    async def handle_retry(update: Update, context: CallbackContext):
        await update.message.reply_text("You can go back and correct your previous inputs by typing 'retry'.")
        # Reset to the previous step (if necessary) based on the current state
        return ConversationHandler.END

    # Cancel the conversation if needed
    async def cancel(update: Update, context: CallbackContext):
        await update.message.reply_text("The process has been canceled.")
        return ConversationHandler.END

    # Handle help command
    async def handle_help(update: Update, context: CallbackContext):
        help_message = (
            "Welcome to the Shipment Management Bot!\n"
            "Here's how you can use the bot:\n"
            "1. 📦 New Shipment: Create a new shipment record.\n"
            "2. 📋 View All Shipments: View all shipments.\n"
            "3. 🔍 View by ID: Look up a shipment by its ID.\n"
            "4. 🆘 Help: Get help information about using the bot."
        )
        await update.message.reply_text(help_message)

    def main():
        # Initialize the application with the bot token
        application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()

        # Define the conversation handler
        conversation_handler = ConversationHandler(
            entry_points=[MessageHandler(filters.Regex('^📦 New Shipment$'), handle_new_shipment)],
            states={
                CUSTOMER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_customer_name)],
                ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address)],
                TRACKING_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_tracking_number)],
                PHOTOS: [MessageHandler(filters.PHOTO | filters.TEXT, handle_photos)],  # Handle both photo uploads and text inputs (skip)
            },
            fallbacks=[CommandHandler('cancel', cancel), MessageHandler(filters.TEXT & ~filters.COMMAND, handle_retry)]  # Retry handling
        )

        # Add handlers
        application.add_handler(conversation_handler)

        # Add message handlers for other options
        application.add_handler(MessageHandler(filters.Regex('^📋 View All Shipments$'), handle_view_all_shipments))
        application.add_handler(MessageHandler(filters.Regex('^🔍 View by ID$'), handle_view_by_id))
        application.add_handler(MessageHandler(filters.Regex('^🆘 Help$'), handle_help))

        # Start polling for updates
        application.run_polling()

    if __name__ == '__main__':
        main()