"""          Author: Mohammed Sadik
             Language: Python 3
             Difficulty: Medium            """

n = input().split()
lim = n[0]
bob = n[1]
count = 0
while True:
    if int(lim) > int(bob):
        break
    elif int(lim) <= int(bob):
        lim = int(lim) * 3
        bob = int(bob) * 2
        count += 1
print(count)
