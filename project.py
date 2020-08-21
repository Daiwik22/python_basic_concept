film = {"Shrek": {"age":0, "seats": 100000000},
       "Next gen": {"age": 0, "seats": 100000000},
       "Endgame": {"age": 11, "seats": 100000000},
       "Bengi": {"age": 5, "seats": 100000000}}

choice = input(
   "Which film would you like to watch? "
   "\n Shrek \n Next gen \n "
   "Endgame \n Bengi "
   "\n Press enter to exit : ").strip().title()
if choice in film:
   if film[choice]["seats"] == 0:
       print("sorry it is sold out \n")

   else:
       age = int(input("How old are you ? : ").strip())
       if age >= film[choice]["age"]:
           no_seats = film[choice]["seats"]
           print("number seats left {} \n".format(no_seats))
           a = int(input("Enter number of seats: "))
           if no_seats > 0:
               if a > no_seats:
                   print("Enter less than or equal to the number of seats available !\n")
               else:
                   no_seats = no_seats - a
                   film[choice]["seats"] = no_seats
                   # print("no. of seats left {}: \n ".format(no_seats))
                   print("Enjoyyyy the movie! \n")

       else:
           print("You are too young to see this movie ! Bye !\n")

else:
   print("Sorry this film does not exist in our list")