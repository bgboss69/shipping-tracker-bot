# File: database.py
from services.google_sheets import GoogleSheetService
from utils.helpers import generate_shipment_id
import datetime

class Database:
    def __init__(self):
        self.sheet_service = GoogleSheetService()

    def create_shipment(self, data):
        """创建货件"""
        data["shipment_id"] = generate_shipment_id()
        # Get current datetime
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # If created_at or updated_at aren't provided, set them
        if "created_at" not in data:
            data["created_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if "updated_at" not in data:
            data["updated_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.sheet_service.create_shipment(data)
        return data["shipment_id"]

    def get_shipment(self, shipment_id):
        """获取货件详情"""
        return self.sheet_service.find_shipment(shipment_id)

    def get_all_shipments(self):
        """Fetch all shipments from the sheet"""
        try:
            shipments = self.sheet_service.get_all_records()
            return shipments
        except Exception as e:
            print(f"Error occurred while fetching all shipments: {e}")
            return []
