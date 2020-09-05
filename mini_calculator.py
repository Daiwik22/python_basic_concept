num1=int(input("Enter number one:"))
num2=int(input("Enter number two:"))
operation=input("Enter type of operation:")

if (operation =="add"):
    print((num1)+(num2))
elif(operation =="sub"):
    print((num1)-(num2))
elif(operation=="multiply"):
    print((num1)*(num2))
elif (operation == "divide"):
    print((num1)/(num2))
else:
    print("Thank you for using mini-calculator")