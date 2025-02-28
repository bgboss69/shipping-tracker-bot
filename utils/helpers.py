# File: utils/helpers.py
import os
import re
from datetime import datetime
from services.google_sheets import GoogleSheetService

# Initialize Google Sheet service
sheet_service = GoogleSheetService()


def generate_shipment_id():
    """生成货件ID（格式：MMDDYY-001）"""
    # Get today's date in MMDDYY format
    today = datetime.now().strftime("%m%d%y")

    # Fetch all records to find the last shipment ID for today
    records = sheet_service.get_all_records()  # Assuming you're calling this method from the correct service
    # print("Fetched Records:", records)

    # Find the last shipment ID for today
    last_shipment_id = None
    for record in records:
        shipment_id = record.get("Shipment ID")
        if shipment_id and shipment_id.startswith(today):
            last_shipment_id = shipment_id

    # print(f"Last Shipment ID: {last_shipment_id}")  # Debug line

    # Extract the numeric part from the last shipment ID (e.g., "001", "002")
    if last_shipment_id:
        match = re.match(r"(\d{6})-(\d{3})", last_shipment_id)  # Regex to match MMDDYY-XXX format
        if match:
            last_number = int(match.group(2))
            new_number = last_number + 1
        else:
            new_number = 1  # If no valid number, start from 1
    else:
        new_number = 1  # If no previous shipment for today, start from 1

    # Format the new number to 3 digits (e.g., 001, 002, ...)
    new_number_str = str(new_number).zfill(3)
    # print(f"New Shipment ID Number: {new_number_str}")  # Debug line

    # Create the new shipment ID
    new_shipment_id = f"{today}-{new_number_str}"
    # print(f"Generated Shipment ID: {new_shipment_id}")  # Debug line

    return new_shipment_id
