# # number=[1,2,3,4,5]
# # print(*number)
# # print(*"abc")
# def add(x,y):
#     return x+y
# def add(*numbers):
#     sum=0
#     for number in numbers:
#         sum+=number
#     return sum
# my_sum=add(1,2,3,4,5,6)
# print(my_sum)
def about(name,age,likes):
    sentence="Meet {}!They are {} years old and they like {}".format(name,age,likes)
    return sentence
my_dict={"name":"anu","age":"10","likes":"python"}
print(about(**my_dict))