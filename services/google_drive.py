# File: services/google_drive.py
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from io import BytesIO
from googleapiclient.http import MediaIoBaseUpload
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GoogleDriveService:
    def __init__(self):
        self.creds = service_account.Credentials.from_service_account_file(
            os.path.join(os.path.dirname(__file__), '../credentials.json'),
            scopes=["https://www.googleapis.com/auth/drive"]
        )
        self.service = build("drive", "v3", credentials=self.creds)

    def upload_photo(self, file_bytes, shipment_id):
        """上传照片到Google Drive并使其公开可访问，删除已有同名文件"""
        # # Find and delete any existing file with the same shipment_id
        # self._delete_existing_file(shipment_id)

        # Create the file metadata
        file_metadata = {
            "name": f"{shipment_id}.jpg",
            "parents": [os.getenv("GOOGLE_DRIVE_FOLDER_ID")]
        }
        
        # Create the media upload object
        media = MediaIoBaseUpload(
            BytesIO(file_bytes),
            mimetype="image/jpeg",
            resumable=True
        )
        
        # Upload the new file
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id, webViewLink"
        ).execute()

        # Set the file permissions to be publicly accessible
        file_id = file["id"]
        self.service.permissions().create(
            fileId=file_id,
            body={
                "role": "reader",  # "reader" means anyone with the link can view
                "type": "anyone"  # "anyone" means public access
            }
        ).execute()

        # Return the public link to the file
        return file["webViewLink"]

    def _delete_existing_file(self, shipment_id):
        """删除已有同名文件"""
        query = f"name = '{shipment_id}.jpg' and '{os.getenv('GOOGLE_DRIVE_FOLDER_ID')}' in parents"
        results = self.service.files().list(q=query, fields="files(id)").execute()
        
        # If a file with the same name exists, delete it
        files = results.get("files", [])
        if files:
            for file in files:
                self.service.files().delete(fileId=file["id"]).execute()

# import os
# from googleapiclient.discovery import build
# from google.oauth2 import service_account
# from io import BytesIO
# from googleapiclient.http import MediaIoBaseUpload
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()


# class GoogleDriveService:
#     def __init__(self):
#         self.creds = service_account.Credentials.from_service_account_file(
#             os.path.join(os.path.dirname(__file__), '../credentials.json'),
#             scopes=["https://www.googleapis.com/auth/drive"]
#         )
#         self.service = build("drive", "v3", credentials=self.creds)

#     def upload_photo(self, file_bytes, shipment_id):
#         """上传照片到Google Drive并使其公开可访问"""
#         # Create the file metadata
#         file_metadata = {
#             "name": f"{shipment_id}.jpg",
#             "parents": [os.getenv("GOOGLE_DRIVE_FOLDER_ID")]
#         }
        
#         # Create the media upload object
#         media = MediaIoBaseUpload(
#             BytesIO(file_bytes),
#             mimetype="image/jpeg",
#             resumable=True
#         )
        
#         # Upload the file
#         file = self.service.files().create(
#             body=file_metadata,
#             media_body=media,
#             fields="id, webViewLink"
#         ).execute()

#         # Set the file permissions to be publicly accessible
#         file_id = file["id"]
#         self.service.permissions().create(
#             fileId=file_id,
#             body={
#                 "role": "reader",  # "reader" means anyone with the link can view
#                 "type": "anyone"  # "anyone" means public access
#             }
#         ).execute()

#         # Return the public link to the file
#         return file["webViewLink"]


# class GoogleDriveService:
#     def __init__(self):
#         self.creds = service_account.Credentials.from_service_account_file(
#             os.path.join(os.path.dirname(__file__), '../credentials.json'),
#             scopes=["https://www.googleapis.com/auth/drive"]
#         )
#         self.service = build("drive", "v3", credentials=self.creds)

#     def upload_photo(self, file_bytes, shipment_id):
#         """上传照片到Google Drive"""
#         file_metadata = {
#             "name": f"{shipment_id}.jpg",
#             "parents": [os.getenv("GOOGLE_DRIVE_FOLDER_ID")]
#         }
#         media = MediaIoBaseUpload(
#             BytesIO(file_bytes), 
#             mimetype="image/jpeg",
#             resumable=True
#         )
        
#         file = self.service.files().create(
#             body=file_metadata,
#             media_body=media,
#             fields="webViewLink"
#         ).execute()
        
#         return file.get("webViewLink")