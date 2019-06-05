#lists In python, lists are part of the standard language. You will find them everywhere.
# Like almost everything in Python, lists are objects. There are many methods associated to
# them. Some of which are presented here below.
#https://thomas-cokelaer.info/tutorials/python/data_structures.html

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
a.extend([2])
print("length of a is {0}, numbers of 2 is {1} ".format(len(a),a.count(2)))
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a += [1,4]
print(a)
b = [1,2,3,4,5]
print(b)
print(b[2:])
print(b[:2])
print(b[:-1])
print(b[-3:])
for i in b:
    print("{} is the number now".format(i))

