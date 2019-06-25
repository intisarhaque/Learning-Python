with open("binary", 'bw') as binFile:
    for i in range(1,17):
        binFile.write(bytes([i]))

with open("binary", 'br') as binFile:
    for i in binFile:
        print(i)

print(bytes([12]))


