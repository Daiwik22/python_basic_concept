
# dict_1[2]=4
# dict_1[5]=25

x=input("Enter lower range number:\t")
y=input("Enter upper range number:\t")
dict_1={}
for i in range(int(x),int(y)):
 # print(i * i)
    dict_1[i]=i * i
print(dict_1)