#dictionaries are key+pair
a = {"a":1, "b":2}
print(a)
print(a.keys())
print(a.values())
print(a["a"])
print(a.items())#list of 2 indexes -> tuple of 2 indexes
print("{} \t {}".format(("a" in a), "c" in a))
a.pop("b")
print(a)
a["c"] = 3
a["b"] = 2
print(a)
a["a"] = 0
print(a)
a.update({"d":4, "e":5})
print(a)
a.update({"a":1})
print(a)
b=a
del(b["a"])
print("{}\n{}".format(a, b))
c=a.copy()
del(c["b"])
print("{}\t{}\t{}".format(a, b, c))
for letter in a.keys():
    print("Letter is {}".format(letter))
for number in a.values():
    print("number is {}".format(number))


