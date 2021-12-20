# 3.1: Names
names = ['scott lamb', 'luke skywalker', 'yoda', 'jean-luc picard']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# 3.2: Greetings
names = ['scott lamb', 'luke skywalker', 'yoda', 'jean-luc picard']
message = "Hello, {}".format(names[0].title())
print(message)
message = "Hello, {}".format(names[1].title())
print(message)
message = "Hello, {}".format(names[2].title())
print(message)
message = "Hello, {}".format(names[3].title())
print(message)

# 3.3: Your Own List
animals = ['dog', 'cat', 'horse', 'chicken']
message = "The breed of {} that I have is a siberian husky.".format(animals[0])
print(message)
message = "I have never been fond of {}s.".format(animals[1])
print(message)
message = "I have riden a {} at least once in my life.".format(animals[2])
print(message)
message = "I like to eat {}.".format(animals[3])
print(message)

# 3.4: Guest List
guests = ['wanda maximoff', 'natasha romanova', 'wonder woman']
print("{}, Would you like to come to dinner with me?".format(guests[0].title()))
print("{}, Would you like to come to dinner with me?".format(guests[1].title()))
print("{}, Would you like to come to dinner with me?".format(guests[2].title()))

# 3.5: Changing the Guest List
print(guests)
print(guests[2].title())
guests[2] = 'gamora'

print("{}, Would you like to come to dinner with me?".format(guests[0].title()))
print("{}, Would you like to come to dinner with me?".format(guests[1].title()))
print("{}, Would you like to come to dinner with me?".format(guests[2].title()))

# 3.6: More Guests
print(guests)
guests.insert(0, 'iron man')
guests.insert(2, 'thor')
guests.append('bruce banner')
print(guests)
print("{}, Would you like to come to dinner with me?".format(guests[0].title()))
print("{}, Would you like to come to dinner with me?".format(guests[1].title()))
print("{}, Would you like to come to dinner with me?".format(guests[2].title()))
print("{}, Would you like to come to dinner with me?".format(guests[3].title()))
print("{}, Would you like to come to dinner with me?".format(guests[4].title()))
print("{}, Would you like to come to dinner with me?".format(guests[5].title()))

# 3.7: Shrinking the Guest List
print(guests)
print("I'm sorry. I'm only able to send out invitations to two individuals")
poppedGuest = guests.pop()
print("I'm sorry, {}. I can no longer invite you to dinner.".format(poppedGuest.title()))
poppedGuest = guests.pop()
print("I'm sorry, {}. I can no longer invite you to dinner.".format(poppedGuest.title()))
poppedGuest = guests.pop()
print("I'm sorry, {}. I can no longer invite you to dinner.".format(poppedGuest.title()))
poppedGuest = guests.pop()
print("I'm sorry, {}. I can no longer invite you to dinner.".format(poppedGuest.title()))
print("You're still invited to dinner, {}.".format(guests[0].title()))
print("You're still invited to dinner, {}.".format(guests[1].title()))
del guests[0]
del guests[0]
print(guests)

# 3.8: Seeing the World
locations = ['england', 'iceland', 'greenland', 'china', 'australia']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# 3.9: Dinner Guests
guests = ['wanda maximoff', 'natasha romanova', 'wonder woman']
print("I'll be inviting {} guests to dinner.".format(len(guests)))