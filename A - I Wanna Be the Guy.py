"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                  """

max = int(input())
x = input().split()
y = input().split()
check = []
test = []
for i in range(1, int(x[0]) + 1):
    if int(x[i]) not in check:
        check.append(int(x[i]))
for i in range(1, int(y[0]) + 1):
    if int(y[i]) not in check:
        check.append(int(y[i]))
for i in range(1, max + 1):
    test.append(i)
check = sorted(check)
if test == check:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
