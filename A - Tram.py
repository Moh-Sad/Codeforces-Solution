"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Medium              """

n = int(input())
check = 0
max = 0
for i in range(n):
    out, In = map(int, input().split())
    check = check - out + In
    if check > max:
        max = check
print(max)
