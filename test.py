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
"""
Intro --> Y -->  successful_entry() --> load_cylce_data() --> Summary --> Start  
Intro --> N -->  successful_entry() --> retrieve() --> Summary --> Start 
"""
lang = 0
message = "empty_string"


def intro():

    global lang

    if lang == 0:
        func1()
        
    elif lang == 1:
        func2()
       
    elif lang == 2:
        func3()
        
    elif lang == 3:
        func4()
        
    elif lang == 4:
        func5()
        return 


def func1():
    global lang
    print("function_!")
    lang = 2
    intro()


def func2():
    global lang
    print("function_2")
    lang = 3
    intro()


def func3():
    global lang
    print("function_3")
    lang = 4
    intro()


def func4():
    global lang
    print("function_4")
    lang = 5
    intro()


def func5():
    global lang
    print("function_5")
    lang = 6
    intro()


intro()
