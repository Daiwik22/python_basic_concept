known_user = ["Alice", "Bob", "Daiwik", "Rohan", "Srijan", "Saurabh", "Anay", "Sia", "Rishaan"]
user = input("Enter your name:\t")
user = user.strip().capitalize()
if user in known_user:
    user_answer = input("Welcome,would you like to remove yourself from list ????\t")
    option = user_answer.strip().capitalize()
    if option == "Yes":
        known_user.remove(user)
        print(known_user)
    elif option == "No":
        print("OK")
        print(known_user)

elif user not in known_user:
    user_answer = input("Sorry you are not in the list,would you like to add yourself ????\t")
    option = user_answer.strip().capitalize()
    if option in "Yes":

        known_user.append(user)
        print(known_user)
        print("Ok")

    elif option == "No":
        print("OK")
        print(known_user)
