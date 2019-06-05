a = (1,2,3)
print(a)
a*=5
print(a)
a = (1,2,3)
print(a)
b = (4,5,6,6)
a += b
print(a)
print("{}\t{}\t{}".format(a.count(6), a.index(4), len(a)))
print("{}\t{}\t{}".format(a[2:], a[:2], a[:-1]))
b = (1,2,[3,4])
print(b)
b[2][0] =5
print(b)
print(str(b))
print(max(a))
