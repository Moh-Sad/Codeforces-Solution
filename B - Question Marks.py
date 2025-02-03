"""     Author: Mohammed Sadik
        Language: Python 3
        Difficulty: Easy     """

for _ in range(int(input())):
    max = int(input()) * 4
    items = list(input())
    check = int(max / 4)
    ans = 0
    if items.count("A") >= check:
        ans += check
    elif items.count("A") < check:
        ans += items.count("A")
    if items.count("B") >= check:
        ans += check
    elif items.count("B") < check:
        ans += items.count("B")
    if items.count("C") >= check:
        ans += check
    elif items.count("C") < check:
        ans += items.count("C")
    if items.count("D") >= check:
        ans += check
    elif items.count("D") < check:
        ans += items.count("D")
    print(ans)
