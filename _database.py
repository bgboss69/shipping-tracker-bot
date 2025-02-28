# import os
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from datetime import datetime

# class Database:
#     def __init__(self):
#          # Ensure the os module is imported
#         scope = ['https://spreadsheets.google.com/feeds',
#                  'https://www.googleapis.com/auth/drive']
#         creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
#         client = gspread.authorize(creds)
#         self.sheet = client.open_by_key(os.getenv('GOOGLE_SHEET_ID')).sheet1

#     def create_shipment(self, data):
#         # 生成ID的逻辑
#         now = datetime.now()
#         base_id = now.strftime("%m%d%y")
#         existing = self.sheet.col_values(1)
#         count = len([x for x in existing if x.startswith(base_id)]) + 1
#         shipment_id = f"{base_id}-{count:03d}"

#         # 添加数据到表格
#         row = [
#             shipment_id,
#             data['customer_name'],
#             data['address'],
#             data['tracking_number'],
#             'Pending Review',
#             datetime.now().isoformat(),
#             ','.join(data['photos']),
#             datetime.now().isoformat()
#         ]
#         self.sheet.append_row(row)
#         return shipment_id

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
class Database:
    def __init__(self):
        # Google Sheets setup
        self.spreadsheet_id = os.getenv('GOOGLE_SHEET_ID')  # Pull from environment variable
        self.sheet_name = 'Sheet1'  # Hardcoded as Sheet1
        
        # Ensure the os module is imported and configured for authentication
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open_by_key(self.spreadsheet_id).worksheet(self.sheet_name)

    def get_spreadsheet_id(self):
        return self.spreadsheet_id

    def get_sheet_name(self):
        return self.sheet_name

    def create_shipment(self, data):
        # ID generation logic
        now = datetime.now()
        base_id = now.strftime("%m%d%y")
        existing = self.sheet.col_values(1)
        count = len([x for x in existing if x.startswith(base_id)]) + 1
        shipment_id = f"{base_id}-{count:03d}"

        # Add data to sheet
        row = [
            shipment_id,
            data['customer_name'],
            data['address'],
            data['tracking_number'],
            'Pending Review',
            datetime.now().isoformat(),
            ','.join(data['photos']),
            datetime.now().isoformat()
        ]
        self.sheet.append_row(row)
        return shipment_id

    def update_shipment_photos(self, shipment_id, photos):
        # Find the row with the given shipment_id
        cell = self.sheet.find(shipment_id)
        if cell:
            row = cell.row
            # Update the photos column (assuming the photos are in column G, index 7)
            self.sheet.update_cell(row, 7, ','.join(photos))
        else:
            print(f"Shipment ID {shipment_id} not found.")
