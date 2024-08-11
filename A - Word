"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Easy    """

List = input()
Original = List
low = 0
high = 0
List = [ item.split() for item in List]
List_num = len(List)
for i in range(1):
    for j in range(List_num):
        if List[j][i] == List[j][i].upper():
            high += 1
        else:
            low += 1
if high > low:
    print(Original.upper())
else:
    print(Original.lower())
