

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pull"), (2, "Psycho"), (3, "Mayhem"))
print(imelda)
album, artist, year, tracks = imelda
print(album, artist, year, tracks)
print("{}\n{}\n{}".format(album, artist, year))
for i in tracks:
    print(i, end='\t')

a = b = c = d = 12;
print(b)
a,c, = 11, 13
print(a, c)
post = "leave", "banger", 10
print(post)
song, status, score = post
print("{}\n{}\n{}".format(song, status, score))

kanye = "MDBTF", 2009
print (kanye)
#kanye[0] = "MBDTF"
#print (kanye)
kanye = "MBDTF", kanye[1] #looks from right to left to evaluate kanye[1] onto new kanye
print (kanye)
kanye2 = ["TLOB", 2016]
print(kanye2)
kanye2[0] = "TLOP"
print(kanye2)

o = range(0,100,4)
print(o)
p = o[::5]
print(p)


r = range(0,100)
print(r)
for i in r:
    print (i, end=' ')
print(" ")
for i in r[::-2]:
    print (i, end=' ')


even = list(range(0,20,2))
print(even)
odd = list(range(1, 1000,2))
print(odd)
print(odd.index(41))
print(odd[20])
range = odd[1:1000:4]
print (range)


string = "12345612345"
string = ("in", "ti", "sar")
my_iterator = iter(string)
for i in range(0,len(string)):
    print(next(my_iterator))





menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
menu.append(['joy', 'egg', 'bacon'])

for meal in menu:
    if not "spam" in meal:
        print (meal)
        for ingredient in meal:
            print (ingredient)


even = [2,4,6,8]
sameEven = even
sameEven.sort(reverse=True)
print(even)
anotherEven = list(even)
anotherEven.sort()
print("{} \n{}".format(even, anotherEven))
sameEven.sort()
print("{} \n{}".format((anotherEven is sameEven), (anotherEven == sameEven)))


ipAddress = input("Enter an IP address ")
print(ipAddress.count("."))

groceryList = ["jelly", "custard", "eggs", "mustard"]
for food in groceryList:
    print("The grocey is {}".format(food))
print("")
groceryList.append("soysauce")
for food in groceryList:
    print("The grocey is {}".format(food))
print("")

groceryListTwo = ["fish", "beans"]
for food in groceryListTwo:
    print("The grocey is {}".format(food))
print("")

groceryListThree = groceryList + groceryListTwo
for food in groceryListThree:
    print("The grocey is {}".format(food))
print("")

groceryListFour = {"yam", "oatcakes", "cream"}
groceryListFive = [groceryListThree, groceryListFour]
print(groceryListFive)

for groceryListSet in groceryListFive:
    print(groceryListSet)
    for items in groceryListSet:
        print(items)

priceList = [1,5,3,9]
print(sorted(priceList))
print(priceList)
priceList.sort()
print(priceList)
