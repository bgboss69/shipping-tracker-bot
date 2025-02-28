```markdown
# Shipment Management Bot 🚚

A Telegram bot for managing shipments with Google Sheets & Drive integration.

![Bot Demo](Demo.gif) <!-- Add actual demo gif later -->

## Features ✨
- **Multi-step shipment creation**
- **Photo upload to Google Drive**
- **Real-time spreadsheet updates**
- **Interactive menu system**
- **Error handling & validation**

## Tech Stack 💻
- Python 3.10+
- python-telegram-bot
- Google Sheets API
- Google Drive API
- gspread

## Installation ⚙️

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/shipping-tracker-bot.git
cd shipment-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Google API Setup 🔑
1. Create Google Cloud Project
2. Enable **Sheets API** & **Drive API**
3. Create Service Account → Download `credentials.json`
4. Place in project root

### 4. Configure Environment
Create `.env` file:
```ini
TELEGRAM_TOKEN=your_bot_token
SPREADSHEET_ID=your_sheet_id
GOOGLE_DRIVE_FOLDER_ID=your_folder_id
```

### 5. Share Resources
- Share Google Sheet with service account email
- Share Drive folder with service account email

## Usage 🚀

### Basic Commands
| Command       | Action                     |
|---------------|----------------------------|
| /start        | Show main menu             |
| /help         | Display help information   |
| /cancel       | Cancel current operation   |

### Workflow Example
1. **Create Shipment**
   ```
   📦 New Shipment → Name → Address → Tracking# → Photos → Done!
   ```
2. **View Shipments**
   ```
   📋 View All → Scroll through list
   🔍 View by ID → Enter shipment ID
   ```

## Folder Structure 📁
```
shipment-bot/
├── bot.py
├── database.py
├── google_api.py
├── credentials.json
├── handlers/
│   ├── create_handler.py
│   ├── view_handler.py
│   └── common_handler.py
├── services/
│   ├── google_sheets.py
│   └── google_drive.py
├── utils/
│   └── helpers.py
└── .env.example
```

## Troubleshooting 🔧
**Common Issues**
- "Permission denied" errors → Re-share resources
- Missing .env variables → Verify all variables set
- API quota exceeded → Check Google Cloud Console

## Contributing 🤝
1. Fork repository
2. Create feature branch
3. Submit PR with detailed description

## License 📄
MIT License - See [LICENSE](LICENSE) for details
```

**Key Elements Included:**
1. Clear visual hierarchy with emojis
2. Step-by-step setup instructions
3. Command reference table
4. Workflow visualization
5. File structure overview
6. Common solutions for typical issues
7. Contribution guidelines template

Would you like me to add any specific sections or modify existing content?