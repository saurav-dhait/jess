import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time
# Define the scope and authenticate with Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('iot123.json', scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by title or by key
spreadsheet = client.open("IoT123")  # or use .open_by_key("your_spreadsheet_key")

# Select the sheet to work with (e.g., the first sheet)
sheet = spreadsheet.sheet1

#Upload some data (example: adding rows to the sheet)

data = [
    ["Name", "Age", "City"],
    ["ABC", str(datetime.now()), "Nagpur"],
    ["XYZ", "65", "Mumbai"],
]

# Update the sheet with the data
for row in data:
    sheet.append_row(row)

print("Data uploaded successfully!")