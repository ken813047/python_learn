
def menus(food):
    if len(food) > 5:
        print("It's a very long",food)
    else:
        print(food)
menu=("curry","rice","chicken","fried chicken","pig")
for food in menu:
    menus(food)
#check_food("curry")
#check_food("rice")
#check_food("chicken")
#check_food("fried chicken")
#check_food("pig")
def double(number):
    return number *2
result = double(2)

print (result)