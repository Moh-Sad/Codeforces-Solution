"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Easy               """

items = list( map(int, input()))
team_1 = 0
team_2 = 0
for i in range(len(items)):
    if items[i] == 0:
        team_1 += 1
        team_2 = 0
    if team_1 >= 7:
        break
    if items[i] == 1:
        team_2 += 1
        team_1 = 0
    if team_2 >= 7:
        break
if team_1 >= 7 or team_2 >= 7:
    print("YES")
else:
    print("NO")
