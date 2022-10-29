current_cycle = ['1', '4', '3', '6', '7']
temp_cycle = ['1', '4', '3', '6', '7']



def testing():
    global current_cycle
    print("Please enter the Cycle Temperatures")
    print("Enter Ten Values Between 0-300 degress")
    print("Seperate the Values by a Comma (,)")
    current_cycle = input("Enter Here: ")
    temp_cycle = current_cycle.split(",")
    temp_cycle = [int(i) for i in temp_cycle]
    print(f"{temp_cycle}")
    

def is_number(n):
    try:
        float(n)  
    except ValueError:
        return False
    return True


testing()
is_number(temp_cycle)