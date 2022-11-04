import statistics
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
function = 0
current_data = "blank"

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
    check_answer_intro(answer_1)
    return


def main():
    global function
 
    if function == 1:
        load_cylce_data()  
    elif function == 3:
        data_analysis()
    elif function == 4:
        store_data
    

def intro_short():
    global failcount

    if failcount < 3:
        print(f"failed Attempts{failcount}")
        print("Do you want to Input new Temperature Readings ?")
        answer_1 = input("Enter your answer here using the Y or N Key : ")
        print(f"You have Answered {answer_1}")
        check_answer_intro(answer_1)
    else:

        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("WARNING CAFFEINE LEVELS LOW ")
        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("You Have Enter Data Wrong 3 Times")
        print("Looks like you need some coffee")
        print("Please come back later more alert")
        failcount = 0

        intro()
        
    return
 

def load_cylce_data():

    global function
    global current_data

    print("Please enter the Cycle Temperatures")
    print("Enter Ten Values Between 0-300 degress")
    print("Seperate the Values by a Comma (,)")
    current_cycle = input("Enter Here: ")
    current_data = current_cycle.split(",")
    print(f"{current_data}")
    validate_data(current_data)
    if validate_data(current_data):
        print("data_Ok")
        function = 3
        main()
    else:
        print("data_NOk")
        function = 1 
        main()


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    global function

    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def data_analysis():
    global function
    global current_data
    print("Data Analysis")
    print(f"{current_data}")
    list_of_integers = list(map(int, current_data))
    print(f"{list_of_integers}")
    total = sum(list_of_integers)
    print(total)
    mean = total/10
    print(f"Start Temperature =: {list_of_integers[0]}")
    print(f"Average Temperature =: {mean}")
    print(f"End Temperature =: {list_of_integers[9]}")
    temp_max = max(list_of_integers) 
    print(f"Max Temp =: {temp_max}")
    temp_min = min(list_of_integers) 
    print(f"Min Temp =: {temp_min}")
    temp_range = temp_max - temp_min
    print(f"Range =: {temp_range}")

    return

def store_data():


    return


def check_answer_intro(answer_1):
    global function
    print(f"This is answer 1{answer_1}")
    if answer_1 == ("Y"):
        function = 1
        return 
    if answer_1 == ("N"):
        function = 2
        return
    else:
        print("Data Entered Incorrect")
        count_fail()
        intro_short()
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
main()
