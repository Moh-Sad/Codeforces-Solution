"""    Author: Mohammed Sadik
       Language: Python 3
       Difficulty: Medium    """

List = input().lower()
new = []
List = [item.split() for item in List]
List_num = len(List)
for i in range(1):
    for j in range(List_num):
          if List[j][i] not in new:
             new.append(List[j][i])
new_num = len(new)
if new_num % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
