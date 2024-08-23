"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Easy              """

year = input()
convert = int(year) + 1
year = str(convert)
while True:
    if int(year[2]) == int(year[3]):
        convert = convert + 1
        year = str(convert)
    elif int(year[1]) == int(year[3]):
        convert = convert + 1
        year = str(convert)
    elif int(year[1]) == int(year[2]):
        convert = convert + 1
        year = str(convert)
    elif int(year[0]) == int(year[3]):
        convert = convert + 1
        year = str(convert)
    elif int(year[0]) == int(year[2]):
        convert = convert + 1
        year = str(convert)
    elif int(year[0]) == int(year[1]):
        convert = convert + 1
        year = str(convert)
    else:
        break
print(year)
