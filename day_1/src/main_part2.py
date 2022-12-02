with open("input.txt", "r") as f:
    calories = f.read().splitlines()

top_three = [0, 0, 0]
current_calories = 0
for calorie in calories:
    print(calorie)
    if calorie == "":
        if current_calories > min(top_three):
            top_three = sorted(top_three)[1:]
            top_three.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(calorie)
print(sum(top_three))
