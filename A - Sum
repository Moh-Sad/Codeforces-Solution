"""      Author: Mohammed Sadik
         Language: Python 3
         Difficulty: Easy        """

n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
list2 = [items.split() for items in list1]
for i in range(n):
    if int(list2[i][0]) == int(list2[i][1]) + int(list2[i][2]):
        print("YES")
    elif int(list2[i][1]) == int(list2[i][0]) + int(list2[i][2]):
        print("YES")
    elif int(list2[i][2]) == int(list2[i][1]) + int(list2[i][0]):
        print("YES")
    else:
        print("NO")
