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

answer_1 = "h"
answer_2 = "g"

records = SHEET.worksheet('Records')

data = records.get_all_values()


def intro():
    print("Welcome to the Temperature Analyis Program\n")
    print("The Program Allows for the following,")
    print("Data Retrieve from Google Sheets")
    print("Data analysis of new input data or retrieved data ")
    print("Do you want to Input new Temperature Readings ?")
    answer_1 = input("Enter your answer here using the Y or N Key : ")
    print(f"You have Answered {answer_1}")
    check_answer_1(answer_1)

    return


def load_cylce_data():
    print("Please enter the Cycle Temperatures")
    print("Enter Ten Values Between 0-300 degress")
    print("Seperate the Values by a Comma (,)")
    current_cycel = input("Enter Here: ")
    print(f"{current_cycel}")
    return


def view_data():
    print("Please Enter the Data Number you want to View")
    print("Enter values between 1 and 10")
    val_requested = input("Enter Here: ")
    print(f"{val_requested}")
    get_line_data(val_requested)

    return


def get_line_data(val_requested):
    values_list = records.row_values(val_requested)
    print(f"{values_list}")
    item_1 = values_list[0]
    item_2 = values_list[1]
    print(f"{item_1},{item_2}")
    return 


def validate_data():
    print("bothing")
    return


def data_analysis():

    return


def check_answer_1(answer_1):
    if answer_1 == ("Y"):
        print("You have Enter Yes")
        load_cylce_data()
    if answer_1 == ("N"):
        print("You have Enter N")
        print("Do you want to Retrive Data for analysis ?")
        answer_2 = input("Enter your answer here using the Y or N Key :")
        check_answer_2(answer_2)

    return


def check_answer_2(answer_2):
    if answer_2 == ("Y"):
        view_data()

    if answer_2 == ("N"):
        intro()
    return


intro()