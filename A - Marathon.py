"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Medium        """

n = int(input())
list1 = []
list2 = []
front = 0
for i in range(n):
    list1.append(input())
list2 = [items.split() for items in list1]
for i in range(n):
    if int(list2[i][0]) < int(list2[i][1]):
        front += 1
    if int(list2[i][0]) < int(list2[i][2]):
        front += 1
    if int(list2[i][0]) < int(list2[i][3]):
        front += 1
    print(front)
    front = 0
