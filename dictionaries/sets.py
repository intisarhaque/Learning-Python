#create program that takes text, returns list of all chars that arent vowels in alphabetcical order
#either take text from keyboard or inbuilt string. wow

theirWord = input("Type in a word so I can return constanants")
constanants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

a = set(theirWord)
print(a)
b = frozenset(constanants)
print(a.intersection(b))
c=frozenset(vowels)
print(sorted(a.difference(c)))






# a = set(range(0,40,2))
# print(a)
# b = set([2,4,6,8])
# print(a.issuperset(b))
# print(a.issubset(b))
#
#
# even = frozenset(range(0,100,2))
# print(even)
#







