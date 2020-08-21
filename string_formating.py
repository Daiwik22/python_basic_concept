name=input("Please enter your name: ")
product=input("Please enter product you want to buy: ")
unitprice = input("Please enter unit price of product: ")
totalMoney = input("Please enter how much money you have: ")
quantity = int(totalMoney)//int(unitprice)
money_left=int(totalMoney)%int(unitprice)

print("Hi {}.Your product is {}."
     "Price of each product is {}."
     "You have total money {}."
     "Hence you can bring {} number of product {}.You will be left with money {} ".format(name,product,unitprice,totalMoney,quantity,product,money_left))