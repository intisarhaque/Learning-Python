
powers=[]
for power in range(15,-1,-1):
    powers.append(2**power)

print(powers)

x = int(input("Please enter a number: "))

for power in powers:
    print(x, end = ' ')
    print(x // power, end=' ')
    x %= power



