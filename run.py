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


def intro():
    """
    Welcome and Brief Description of What program does 
    Asks User First Question and Calls Checking of Answer
    """
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
    check_answer_intro(answer_1)
    return


def main():
    """
    Main Rountine Used to Navigate through the Program depending on what
    User inputs and wether it is valid or not 
    """
 
    if function == 1:
        load_cylce_data()  
    elif function == 2:
        data_retrieve()
    elif function == 3:
        data_analysis()
    

def intro_short():
    """
    Rountine Used to restart the programs without long intro 
    """
    global failcount

    if failcount < 3:
        print("\n")
        print("\n")
        print("Do you want to Input new Temperature Readings ?")
        answer_1 = input("Enter your answer here using the Y or N Key : ")
        check_answer_intro(answer_1)
        main()
    else:

        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("WARNING CAFFEINE LEVELS LOW ")
        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("You Have Entered Y/N Data Wrong 3 Times")
        print("Looks like you need some coffee")
        print("Please come back later more alert")
        failcount = 0
        intro_short()
  
    return
 

def load_cylce_data():
    """
    Takes in the User Data for a Temperature Cycle,
    Validates it and then calls analysis function
    """

    global function
    global current_data

    print("Please enter the Cycle Temperatures - 10 Entries Required")
    print("Seperate the Values by a Comma (,)")
    current_cycle = input("Enter Here: ")
    current_data = current_cycle.split(",")
    print(f"{current_data}")
    validate_data(current_data)
    if validate_data(current_data):
        print("data input Ok")
        function = 3
        main()
    else:
        print("data input nOk")
        function = 1 
        main()
    return


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 10 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 10:
            raise ValueError(
                f"Exactly 10 values required, you provided {len(values)}"
            )
            return False
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_data_single(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 10 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                f"Exactly 1 values required, you provided {len(values)}"
            )
            return False
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def data_analysis():
    """
    Analyse the Data input and returns information to the operator
    Once Done Program loops to Short intro
    """
    global function
    global current_data
    list_of_integers = list(map(int, current_data))
    print("-------------------------------------------------")
    print("-------------------------------------------------\n")
    print(f"Data to be analysed =: {list_of_integers}")
    print("-------------------------------------------------")
    print("-------------------------------------------------\n")
    list_of_integers = list(map(int, current_data))
    total = sum(list_of_integers)
    mean = total/10
    temp_max = max(list_of_integers) 
    temp_min = min(list_of_integers) 
    temp_range = temp_max - temp_min
    print(f"Start Temperature =: {list_of_integers[0]}")
    print(f"End Temperature =: {list_of_integers[9]}")
    print(f"Average Temperature =: {mean}")
    print(f"Max Temp =: {temp_max}")
    print(f"Min Temp =: {temp_min}")
    print(f"Range =: {temp_range}")

    intro_short()

    
def check_answer_intro(answer_1):
    """
    Check Y or N answer and define next function to be called. 
    or if incorrect data then count failure and retry 
    """
    global function
    
    if answer_1 == ("Y"):
        function = 1
        return 
    if answer_1 == ("N"):
        function = 2
        return
    else:
        print("Answered Entered Incorrect")
        print('You must answer useing "Y" or "N" ')
        count_fail()
        intro_short()
    return


def check_answer_rcv(answer_2):
    """
    Check Y or N answer and define next function to be called. 
    or if incorrect data then count failure and retry 
    """
    global function
    
    if answer_2 == ("Y"):
        get_data_gspread()
        return 
    if answer_2 == ("N"):
        intro_short()
    else:
        print("Answered Entered Incorrect")
        print('You must answer useing "Y" or "N" ')
        count_fail()
        data_retrieve()
    return


def data_retrieve():

    global failcount

    if failcount < 3:
        print("\n")
        print("\n")
        print("Do you want to retrieve Temperature Readings ?")
        answer_2 = input("Enter your answer here using the Y or N Key : ")
        check_answer_rcv(answer_2)
    else:

        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("WARNING CAFFEINE LEVELS LOW ")
        print("-------------------------------------------------")
        print("-------------------------------------------------\n")
        print("You Have Entered Y/N Data Wrong 3 Times")
        print("Looks like you need some coffee")
        print("Please come back later more alert")
        failcount = 0
        data_retrieve()
  
    return


def get_data_gspread():
    global current_data
    global function
    print("Please choose what data index you want to analyse ?")
    data_id = input("please select number between 1 to 10 :  ")
    validate_data_single(data_id)

    if validate_data_single(data_id) and (data_id > '0'):

        data_rcvd = records.row_values(data_id)
        print(f"data_rcvd{data_rcvd}")
        current_data = data_rcvd
        function = 3 
        main()
    else:
        print(f"{data_id} Not a valid Number")
        get_data_gspread()
    return


def count_fail():
    """
    Counter for Fail Y or N input 
    """
    global failcount
    failcount = failcount + 1
    return


def successful_entry():
    """
    Resets counter for Fail Y or N input 
    after good input 
    """
    global failcount
    failcount == 0
    return


intro()
main()
