"""              Author: Mohammed Sadik
                 Language: Python 3
                 Difficulty: Easy                  """

items = list(input().lower())
Check = "aeoiuy"
constants = []
for i in range(len(items)):
    if items[i] not in Check:
        constants.append(items[i])
for i in range(len(constants)):
    print("." + constants[i], end = "")
