#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return("None")
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def _close_progrram():
    print("Done. Terminating")
    exit()

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice == '+':
        return add
    elif choice == '-':
        return subtract
    elif choice == '*':
        return multiply
    elif choice == '/':
        return divide
    elif choice == '^':
        return power
    elif choice == '%':
        return remainder
    elif choice == '#':
        return _close_progrram
    elif choice == '$':
        pass
    else:
        print("Unrecognized operation")
        



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
def main_menu():
    while True:
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")

        choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
        print(choice)

        if choice not in ['+', '-', '*', '/', '^', '%', '#', '$']:
            print("Invalid choice. Please try again.")
            continue

        if choice == '#':
            _close_progrram()

        if choice == '$':
            continue
     
        try:
            numa = input("Enter first number: ")
            print(numa)
            if numa=="#":
                _close_progrram()
            else:            
                num1 = float(numa)

            numb = input("Enter second number: ")
            print(numb)
            if numb=="#":
                _close_progrram()
            else:
                num2 = float(numb)

            operation = select_op(choice)
            result = operation(num1, num2)
            if result=="None":
                print("float division by zero")
                print(num1, choice, num2, "=", result)
            else:
                print(num1, choice, num2, "=", result)
        except ValueError:
            pass
        except:
            exit()

main_menu()      
#program ends here