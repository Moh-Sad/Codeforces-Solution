"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Medium        """

for _ in range(int(input())):
    n, k = map(int, input().split())
    count = 0
    if n == 1:
        print(0)
    else:
        while n > 1:
            n = n - (k - 1)
            count += 1
        print(count)
