# print("Welcome to the calculator of 2 numbers")
num1=int(input("enter first number:\t"))
num2=int(input("enter second number:\t"))
print("Use opperations from below: \n" "+ - * and /")
operation=input("enter operation:\t")
print("operation:\t"+operation)
if(operation=="+"):
    add_num=int(num1)+int(num2)
    print("Added value is:\t"+str(add_num))
elif(operation=="*"):
    multiply_num=int(num1)*int(num2)
    print("Multiplied value is:\t"+str(multiply_num))
elif(operation=="-"):
    subtract_num=int(num1)-int(num2)
    print("Subtracted value is:\t"+str(subtract_num))
elif(operation=="/" or "Divide" or "Div"):
    divide_num = int(num1)/int(num2)
print("divided value is:\t"+str(divide_num))