# alien = {'color': 'brown', 'points': '10'}
# print(alien['color'])
# print(alien['points'])

# alien['color'] = 'green'
# print("The color of the alien is {}".format(alien['color']))

# greenAlien = {'color': 'green', 'points': 5}
# yellowAlien = {'color': 'yellow', 'points': 10}
# redAlien = {'color': 'red', 'points': 15}

# aliens = [greenAlien, yellowAlien, redAlien]

# for alien in aliens:
#     print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...")