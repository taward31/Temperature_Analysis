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

records = SHEET.worksheet('Records')

data = records.get_all_values()

print("Welcome to the Temperature Analyis Program\n")

print("Do you want to Input new Temperature Readings - Y/N")

answer_1 = input("Enter your answer here using the Y or N Key : ")

print(f"You have Answered {answer_1}")


def load_cylce_data ():
    print("Please enter the Cycle Temperatures")
    print("Enter Ten Values Between 0-300 degress")
    print("Seperate the Values by a Comma (,)")
    current_cycel = input("Enter Here: ")
    print(f"{current_cycel}")

def view_data ():
    print("Please Enter the Data Number you want to View")
    print("Enter values between 1 and 10")
    val_requested = input("Enter Here: ")
    print(f"{val_requested}")

def get_line_data();



def validate_data():




if answer_1 == ("Y"):
    print("You have Enter Yes")

    load_cylce_data()


if answer_1 == ("N"):
    print("You have Enter N")

    view_data()



