"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Medium              """

items = list(input())
count = 0
nearly_lucky = False
for i in range(len(items)):
    if int(items[i]) == 4 or int(items[i]) == 7:
        count += 1
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
