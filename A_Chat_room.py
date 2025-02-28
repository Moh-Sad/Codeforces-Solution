"""      Author: Mohammed Sadik
         Language: Python 3
         Difficulty: Easy      """

items = input()
bag = []
count = 0
for i in items:
    if i == "h" and "h" not in bag:
        bag.append("h")
    elif i == "e" and "e" not in bag and "h" in bag:
        bag.append("e")
    elif i == "l" and count < 2 and "e" in bag:
        bag.append("l")
        count += 1
    elif i == "o" and "o" not in bag and count >= 2:
        bag.append("o")
bag = "".join(bag)
if bag == "hello":
    print("YES")
else:
    print("NO")