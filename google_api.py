import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GoogleDriveService:
    def __init__(self):
        self.creds = service_account.Credentials.from_service_account_file(
            'credentials.json',
            scopes=['https://www.googleapis.com/auth/drive']
        )
        self.service = build('drive', 'v3', credentials=self.creds)

    def upload_photo(self, file_bytes, shipment_id):
        file_metadata = {
            'name': f'{shipment_id}.jpg',
            'parents': [os.getenv('GOOGLE_DRIVE_FOLDER_ID')]
        }
        media = MediaIoBaseUpload(BytesIO(file_bytes), mimetype='image/jpeg')
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='webViewLink'
        ).execute()
        return file.get('webViewLink')

class GoogleSheetService:
    def __init__(self):
        self.creds = service_account.Credentials.from_service_account_file(
            'credentials.json',
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        self.service = build('sheets', 'v4', credentials=self.creds)
    
    def find_shipment_row(self, shipment_id):
        # 使用更高效的批量查询
        result = self.service.spreadsheets().values().get(
            spreadsheetId=os.getenv('GOOGLE_SHEET_ID'),
            range='A2:A'
        ).execute()
        values = result.get('values', [])
        return next((i+2 for i, row in enumerate(values) if row[0] == shipment_id), None)