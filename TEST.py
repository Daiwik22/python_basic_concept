#list_number=("1","2","3")
#for number in list_number:
 #   print(number)
# Write your dog_years function here:
def dog_years(name, age):
    dog_year_age = 7 * age
    return ("{}, I am {} years old in dog years".format(name, dog_year_age))


# Uncomment these function calls to test your dog_years function:
# print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Me", 111))
# should print "Baby, you are 0 years old in dog years"