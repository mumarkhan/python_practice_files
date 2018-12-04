import re

food_items = "butter milk mango banana milk"


# compiling to get pattern object which has
# other methods like sub
regex = re.compile("[m]ilk")
# substituting 'milk' with 'egg'
new_food_items = regex.sub("egg", food_items)
print(new_food_items)
