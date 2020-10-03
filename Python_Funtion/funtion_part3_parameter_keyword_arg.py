def about(name, age, likes="Python"):
    sentence = "Meet {}!He is {} years old and he likes {}".format(name, age, likes)
    return sentence
my_sentence=about(age=23,name="Jack")
print(my_sentence)
