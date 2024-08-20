"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Medium                """

goal = int(input())
count = 0
 
while goal > 0:
    if goal < 5:
        count += 1
        break
    elif  goal >= 5:
        count += 1
        goal -= 5
print(count)
