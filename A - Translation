"""      Author: Mohammed Sadik
         Language: Python 3
         Difficulty: Easy      """

list1 = input().lower()
list1 = [item.split() for item in list1]
list2 = input().lower()
list2 = [item.split() for item in list2]
list2 = list2[::-1]
num = len(list1)
Value = False
for i in range(1):
    for j in range(num):
        if list1[j][i] != list2[j][i]:
            Value = False
            break
        else:
            Value = True
if Value == True:
    print("YES")
else:
    print('NO')
