# 4.1: Pizzas
pizzas = ['cheese', 'pepperoni', 'combo']
for pizza in pizzas:
    print(pizza)
    print("I like {} pizza.\n".format(pizza.title()))
print("I really like pizza.")

# 4.2: Animals
animals = ['dog', 'bird', 'fish']
for animal in animals:
    print(animal.title())
    print("A {} would make a great pet.\n".format(animal.title()))
print("Any of these animals would make a great pet.")

# 4.3: Counting to Twenty
for value in range(21):
    print(value)

# 4.4: One Million
millions = list(range(1000001))
# for value in millions:
#     print(value)

# 4.5: Summing a Million
print(min(millions))
print(max(millions))
print(sum(millions))

# 4.6: Odd Numbers
odds = list(range(1, 21, 2))
for value in odds:
    print(value)

# 4.7: Threes
threes = list(range(3, 31, 3))
for value in threes:
    print(value)

# 4.8: Cubes
cubes = []
for value in range(11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

# 4.9: Cube Comprehension
cubes = [value ** 3 for value in range(11)]
print(cubes)

# 4.10: Slices
print("The first three items in the list are:")
for cube in cubes[:3]:
    print(cube)

print("The middle items are:")
for cube in cubes[3:-3]:
    print(cube)

print("The last three items in the list are:")
for cube in cubes[-3:]:
    print(cube)

# 4.11: My Pizzas, Your Pizzas
pizzas = ['cheese', 'pepperoni', 'combo']
friendPizzas = pizzas[:]

pizzas.append('meat lovers')
friendPizzas.append('veggie')

print("My favorite pizzas are:\n")
for pizza in pizzas:
    print(pizza)
print("\nMy friends favorite pizzas are:")
for pizza in friendPizzas:
    print(pizza)