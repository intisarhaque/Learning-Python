
#https://docs.python.org/3/library/functions.html#open

# wtfisthis = "something", "else", "20324", ((1, "wtf"), (2, "fu"))
#
# with open("wtfisthis.txt", 'w') as jomes:
#     print(wtfisthis, file=jomes)

# with open("wtfisthis.txt", 'r') as jomes:
#     contents=jomes.readline()
#
# wtfisthis = eval(contents)
#
# print(wtfisthis)
# title, artist, year, tracks = wtfisthis
# print(title)
# print(artist)
# print(year)
# print(tracks)

# cities = ["London", "Manchester", "Birmingham"]
#
# with open("cities.txt", 'w') as cityFile:
#     for city in cities:
#         print(city, file=cityFile, flush=True)

# cities = []
#
# with open("cities.txt", 'r') as cityFile:
#     for city in cityFile:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)




# with open("sample.txt", 'r') as jimmer:
    # line = jimmer.readline()
    # print(line)
    # while line:
    #     print(line, end='')
    #     line = jimmer.readline()

    # lines = jimmer.readlines()
    #lines = jimmer.read()
# print(lines)
# for line in lines:
#     print(line, end = '')
#
# for line in lines[::-1]:
#     print(line, end='')
#
#
with open("sample.txt", 'r') as jogger:
    for line in jogger:
        print(line, end = '')
        #print(line)



#
# jobber = open("/Users/arsen/Documents/Learning-Python/EyeOh/sample.txt", 'r')
# jobber = open("sample.txt", 'r')
# for line in jobber:
#     if "jabberwock" in line.lower():
#         print(line, end = '')
#
# jobber.close()
