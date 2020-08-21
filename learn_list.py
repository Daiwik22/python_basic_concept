list_friends=["Narayan","Srijan","Chetan","Rohan"]
print("My first friend is:\t"+list_friends[0])
print("My second friend is:\t"+list_friends[2])
print("My third friend is:\t"+list_friends[3])
print("My forth friend is:\t"+list_friends[1])

# list_number=["0","1","2"]
# print("The first three number  are:\t"+list_number[0])
# print("The first three number  are:\t"+list_number[1])
# print("The first three number  are:\t"+list_number[2])
list_num=input("all numbers separated by hyphen:")
print(type(list_num))
my_list=list_num.split("-")
print(type(my_list))
print(my_list)
print("The first number is :\t"+my_list[0])
print("The second number is :\t"+my_list[1])
#print(len(my_list))

#find the last element of list entered by user using lenth of user list
x=len(my_list) - 1
print("The last number is :\t"+my_list[x])

