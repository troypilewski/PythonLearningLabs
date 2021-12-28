availableToppings = ['cheese', 'pineapple', 'bacon', 'pepperoni', 'onions', 'olives']

requestedToppings = ['cheese', 'pineapple', 'bacon', 'fries']

for topping in requestedToppings:
    if topping in availableToppings:
        print("Adding {}".format(topping))
    else:
        print("This pizza shop does not serve {}".format(topping))
print("Finished making your pizza.")