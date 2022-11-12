import string
import random

list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)

number_of_characters = input("H-how many characters do you want? >=< ")

while True:
    try:
        number_of_characters = int(number_of_characters)
        if number_of_characters < 8:
            print('P-please enter 8 or more!')
            number_of_characters = input("Okay n-now enter 8 or more, you got this! ")
        else:
            break
    except:
        print('Only numbers are allowed, p-please enter a number.')        
        number_of_characters = input("H-how many characters do you want? >=< ")

random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

p1 = round(number_of_characters * (30/100))
p2 = round(number_of_characters * (20/100))

password = []

for i in range(p1):
    password.append(list1[i])
    password.append(list2[i])

for i in range(p2):
    password.append(list3[i])
    password.append(list4[i])

password = "".join(password[0:])        
print (password)