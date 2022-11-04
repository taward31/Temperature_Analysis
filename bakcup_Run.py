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


def intro():
    print("-------------------------------------------------\n")
    print("Welcome to the Temperature Analysis Program\n")
    print("------------------------------------------------\n")
    print("The Program Allows for the following,\n")
    print(" 1 -  Data Loading to Google Sheets for storage ")
    print(" 2 -  Data Analysis of the Temperature Cylce")
    print(" 3 -  Data Retrieving from Sheet for Analysis\n")
    print("-------------------------------------------------")
    print("-------------------------------------------------\n")
    print("Do you want to Input new Temperature Readings ?")
    answer_1 = input("Enter your answer here using the Y or N Key : ")
    print(f"You have Answered {answer_1}")
    check_answer_1(answer_1)

    return


def intro_short():
    if failcount < 3:
        print(f"failed Attempts{failcount}")
        print("Do you want to Input new Temperature Readings ?")
        answer_1 = input("Enter your answer here using the Y or N Key : ")
        print(f"You have Answered {answer_1}")
        check_answer_1(answer_1)
    else:

        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("WARNING CAFFEINE LEVELS LOW ")
        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("You Have Enter Data Wrong 3 Times")
        print("Looks like you need some coffee")
        print("Please come back later more alert")
        
    return


def retrieve():
    if failcount < 3:
        print(f"failed Attempts{failcount}")
        print("Do you want to Retrive Data for analysis ?")
        answer_2 = input("Enter your answer here using the Y or N Key :")
        check_answer_2(answer_2)
        
    else:
        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("WARNING CAFFEINE LEVELS LOW ")
        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("You Have Enter Data Wrong 3 Times")
        print("Looks like you need some coffee")
        print("Please come back later more alert")
        
    return


def load_cylce_data():
    print("Please enter the Cycle Temperatures")
    print("Enter Ten Values Between 0-300 degress")
    print("Seperate the Values by a Comma (,)")
    current_cycle = input("Enter Here: ")
    data = current_cycle.split(",")
    print(f"{data}")
    validate_data(data)
    data_analysis(data)

    return
    

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        if len(values) != 10:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

    return True


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
    value_1 = values_list[0]
    value_2 = values_list[1]
    value_3 = values_list[2]
    value_4 = values_list[3]
    value_5 = values_list[4]
    value_6 = values_list[5]
    value_7 = values_list[6]
    value_8 = values_list[7]
    value_9 = values_list[8]
    value_10 = values_list[9]
    total_value = [value_1 + value_2 + value_3 + value_4 + value_5 + 
                   value_6 + value_7 + value_8 + value_9 + value_10]
    print(f"{total_value}")
    return 


def data_analysis(data):

    print(f"Data Analysis{data}")

    print(f"{data}")
    value_1 = data[0]
    value_2 = data[1]
    value_3 = data[2]
    value_4 = data[3]
    value_5 = data[4]
    value_6 = data[5]
    value_7 = data[6]
    value_8 = data[7]
    value_9 = data[8]
    value_10 = data[9]
    total_value = [value_1 + value_2 + value_3 + value_4 + value_5 + 
                   value_6 + value_7 + value_8 + value_9 + value_10]
    print(f"{total_value}")
    return


def check_answer_1(answer_1):
    if answer_1 == ("Y"):
        successful_entry()
        load_cylce_data()

    if answer_1 == ("N"):
        successful_entry()
        retrieve()
    else:
        print("Data Entered Incorrect")
        count_fail()
        intro_short()
    
    return


def check_answer_2(answer_2):
    if answer_2 == ("Y"):
        successful_entry()
        view_data()

    if answer_2 == ("N"):
        successful_entry()
        intro()
    else:
        print("Data Entered Incorrect")
        count_fail()
        retrieve()
    
    return


def count_fail():
    global failcount
    failcount = failcount + 1
    return


def successful_entry():
    global failcount
    failcount == 0
    return


intro()