#Author Nakshatra Dandgund
#Practicing slicing in python
name=input("Enter your name")
last=name[-1]
second_last=name[-2]
print("The last and second last letter of your name are", last, second_last)
print("The characters in your letter are")
for character in name:
    print(character)
