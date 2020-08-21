# list_number=["0","1","2"]
# print("The first three number  are:\t"+list_number[0])
# print("The first three number  are:\t"+list_number[1])
# print("The first three number  are:\t"+list_number[2])
list_colors=input("All colors separated by comma:\t")
my_list=list_colors.split(",")
print(my_list)
x=len(my_list) - 1
print("The last color in the list is:\t"+my_list[x])