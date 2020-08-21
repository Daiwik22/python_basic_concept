def password_control(my_string):
    if len(my_string)<8:
        return "Daiwik,I am still a genius"
    elif len(my_string)>=8:
        return "Daiwik,I am a genius"
x=password_control("Daiwik")
print(x)
# def weather_condition(temperature):
#     if temperature<30.0:
#         return "cold"
#     elif temperature>=30.0:
#         return "warm"
# z=float(input("Enter temperature of weather:\t"))
# x=weather_condition(z)
# print(x)