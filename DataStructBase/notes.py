#lists In python, lists are part of the standard language. You will find them everywhere.
# Like almost everything in Python, lists are objects. There are many methods associated to
# them. Some of which are presented here below.

a = [1,2,3]
print(a)
a.append(4)
print(a)
a.append([5,6])
print(a)
del a[-1]
print(a)
a.extend([5,6])
print(a)
print(a.index(4))
print(a[5])
a.insert(3, 3.5)
print(a)
a.remove(3.5)
print(a)
a.pop()
print(a)
print("length of a is {}, number of 3 is {}".format(len(a)), a.count(3))