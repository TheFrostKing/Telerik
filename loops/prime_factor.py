longest = 0
longest_food = ""
counter = 1
while counter <= 50:
    food = str(input())
    if food == "END" and counter>=2:
        break
    if longest <= len(food):
        longest_food = food
        longest = len(food)
    counter += 1
print(longest_food)

