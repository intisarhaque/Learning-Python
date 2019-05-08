# ipAdd=input("Enter an ip address    ")
# print(ipAdd)
# count = 0
# for i in range(0,len(ipAdd)):
#     #print(ipAdd[i], end=' ')
#     if ((i==0) & (ipAdd[i]=='.')) or ((i==len(ipAdd)-1) & (ipAdd[i]=='.')):
#         continue
#     elif (ipAdd[i]=='.'):
#         count +=1
# if (ipAdd!=''):
#     print(count+1)
#



# shoppingList = ["milk", "tomato", "eggs"]
# for item in shoppingList:
#     if item == "cheese":
#         print("fuck " + item)
#         break;
# else:
#     print("Buying " + item)


# numberString = "1,2,3,445,6,7,8678,123"
# numberInt = ''
#
# for char in numberString:
#     if char in "123456789":
#         numberInt += char
# print(numberInt)
#
# for state in ["joe","bob", "rush"]:
#     print("what is name {}".format(state))
#
# print (8%7)

# for i in range(1,10):
#     print("penis", end='')
#     print(i)
# print("vaginea")

import random

highest = 1000
x = random.randint(1,highest)
while True:
    i=1;
    print("Guess a number between 1 and {}, 0 to quit".format(highest))
    guess = int(input())
    if guess == 0:
        break
    if guess == x:
        print("You're correct, it took you {} attempts",format(i))
        break;
    elif guess > x:
        print("Too high, try again")
    else:
        print("Too low, try again")
    i+=1