# File: services/google_sheets.py
import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GoogleSheetService:
    def __init__(self):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(os.path.dirname(__file__), '../credentials.json'), scope)

        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(os.getenv("GOOGLE_SHEET_ID")).sheet1

    def find_shipment(self, shipment_id):
        """根据货件ID查找记录"""
        try:
            cell = self.sheet.find(shipment_id)
            if cell is None:  # Just in case .find() returns None
                return None
            return self.sheet.row_values(cell.row)
        except Exception as e:
            print(f"Error occurred while searching for shipment: {e}")
            return None


    def create_shipment(self, data):
        """创建新货件记录"""
        row = [
            data["shipment_id"],
            data["customer_name"],
            data["address"],
            data["tracking_number"],
            ", ".join(data.get("photos", [])),
            "Pending Review",
            data["created_at"],
            data["updated_at"],
             
        ]
        self.sheet.append_row(row)

    def get_all_records(self):
        """Fetch all shipment records"""
        try:
            records = self.sheet.get_all_records()  # Using gspread's built-in get_all_records() method
            # print("Fetched records:", records)  # Print the records for debugging
            return records
        except Exception as e:
            print(f"Error occurred while fetching records: {e}")
            return []
