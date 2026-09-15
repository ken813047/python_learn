foods= ["rice", "curry", "fish", "chicken", "pig"]
print(len(foods))
for food in foods:
    len(food)
    if len(food) > 5:
        print("it's very long:", (food))
    else:
        print(food)