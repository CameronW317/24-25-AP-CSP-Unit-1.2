#list of items
animals_list = ["Dog", "Cat", "Mouse", "Bird", "Monkey", "Honeybadger", "Cheetah", "Deer"]

index = 0
while index < len(animals_list):
    if(index == 3):
        animals_list[3] = "Dog"

    print(animals_list[index])
    index += 1

