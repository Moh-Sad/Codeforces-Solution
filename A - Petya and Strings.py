"""            Author: Mohammed Sadik
               Language: Python 3
               Difficulty: Easy            """

first = list(input().lower())
second = list(input().lower())
if second > first:
    print("-1")
elif second < first:
    print("1")
else:
    print("0")
