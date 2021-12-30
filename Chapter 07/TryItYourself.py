# 7.1: Rental Car
""" makes = ['subaru', 'mercedes-benz', 'honda', 'toyota', 'lexus']

prompt = "These are the available car makes: "
for make in makes:
    prompt += "{}, ".format(make.title())
prompt += "\nEnter your selection: "
make = input(prompt)

print("Let me check if we have a {}.".format(make)) """

# 7.2: Resturant Seating
""" prompt = "How many guests are in your dinner party? "
guests = int(input(prompt))

if guests >= 8:
    print("Please wait while we get your table ready.")
else:
    print("Let me take you to your table.") """

# 7.3: Multiples of Ten
""" prompt = "Enter a number: "

number = int(input(prompt))

if number % 10 == 0:
    print("The number entered is a multiple of ten.")
else:
    print("The number entered is not a multiple of ten.") """