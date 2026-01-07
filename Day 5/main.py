#author: NAkshatra Dandgund
#taking user input
name=input("Enter your name")
product=input("Enter the product name")
price=float(input("Enter the price of the product"))
pieces=int(input("Enter the number of pieces you have bought"))
total_cost=price*pieces
print("-------------- The Bill -----------------------")
print("name :", name)
print("product name", product)
print("The price of the product", price)
print(" the number of", product,"pieces bought",pieces)
print("The total cost =", total_cost)
