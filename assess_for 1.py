# #take numbers input from user seperated by comma.
# #create a for loop and find the sum of all the number using it.
# list_number=input("Enter the numbers separated by a comma:\t")
#for number in list_number:
#     add_num=int(number[0])+int(number[1])+int(number[2])
# print("Added value of all the numbers is:\t"+str(add_num)[x])
sum=0
list_number=input("Enter number separated comma:\t")
my_list=list_number.split(list_number)
for number in my_list:
    sum=sum+(number)


print(sum)
z=(len(my_list))
x=(sum/z)
print(x)

