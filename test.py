import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('package.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Temperature_Cycle_Analysis')

answer_1 = "blank"
answer_2 = "blank"
failcount = 0

records = SHEET.worksheet('Records')
data = records.get_all_values()

numRows = records.row_count  # Get the number of rows in the sheet

print(f"{numRows}")
insertRow = ["11", "22", "33"]
records.insert_row(insertRow, 3)

