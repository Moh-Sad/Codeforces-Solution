"""             Author: Mohammed Sadik
                Language: Python 3
                Difficulty: Medium                """

items = list(input())
check = []
for i in range(1, len(items), 3):
    if items[i] not in check:
        check.append(items[i])
if len(check) == 1 and check[0] == "}":
    print(0)
else:
    print(len(check))
