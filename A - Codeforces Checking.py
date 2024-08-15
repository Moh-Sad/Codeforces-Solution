"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Easy        """

n = int(input())
list1 = []
list2 = ["c", "o", "d", "e", "f", "r", "s"]
for i in range(n):
    list1.append(input())
    if list1[i] in list2:
        print("YES")
    else:
        print("NO")
