def add(a,b):
    return a + b
def sub(a , b):
    return a - b
def multipy(a, b):
    return a * b
def divide(a , b):
    if b!= 0:
        return a / b
    else:
        print("cannot divide by zero ")
try:
    print("=====codveda calculator=====")
    num1 =  int(input("enter first number: "))
    num2 = int(input("enter the second number: "))
    print("SELECT OPERATION ")
    print("1- addition")
    print("2 - subtraction ")
    print("3 - multiplication")
    print("4 - division")

    choice = input("enter choice (1/2/3/4): ")

    if choice == '1':
        print("result: ",add(num1, num2))
    elif choice == '2':
        print("result: ",sub(num1, num2))
    elif choice == '3':
        print("result: ", multipy(num1, num2))
    elif choice == '4':
        print("result: ", divide(num1, num2))
        
    else: 
        print("invalid choice")
except ValueError:
    print("error : please enter a valid number")
except Exception as e:
    print("unexpected error")