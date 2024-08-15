"""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Medium          """"

n = int(input())
list1 = []
list2 = []
list3 = []
front = 0
for i in range(n):
    list1.append(input())
list2 = [items.split() for items in list1]
for i in range(n):
    if int(list2[i][0]) + int(list2[i][1]) >= 10:
                                print("YES")
    elif int(list2[i][0]) + int(list2[i][2]) >= 10:
                                print("YES")
    elif int(list2[i][1]) + int(list2[i][2]) >= 10:
                                print("YES")
    else:
        print("NO")
