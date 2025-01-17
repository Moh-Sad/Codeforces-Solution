"""        Author: Mohammed Sadik
           Language: Python 3
           Difficulty: Easy        """

num, min = map(int, input().split())
count = 1
sum = num
while True:
    if (sum - min) % 10 == 0:
        break
    elif sum % 10 == 0:
        break
    else:
        count += 1
        sum += num
print(count)
