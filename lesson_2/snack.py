#part one all about data types

snack=input("what would you like to order")
price=float(input("what is the price"))
is_available=bool(input("is it available"))
quantity=int(input("how much"))
print(f"you have ordered {snack} which is for {price} amount and you have ordered {quantity} of them whic is available{is_available}")
print("the type of snack is",type(snack))
print("the type of quantity is",type(quantity))
print("the type of price is",type(price))
print("the type of availability is",type(is_available))

#part two is about arithmetic operators
sales=price-0.25
total=quantity*sales
quantity=quantity/2
print(f"you have received a discount of 0.25 the new price is {sales} the total is {total}")

#part 3 is abt comparison operators
print("is price less than 2",price<2)
print("is quantity greater than or equal to 2",quantity >=2)
print("is price equal to 2",price==2)

name=input("what is your name")
print("the first 3 letters of your name is",name[0:3])

print("the last 3 letters of your name is",name[-3:])

print("the 4th letter of your name is",name[3])
print("your name has ", len(name), " characters")
print(name+" has ordered a "+snack)
