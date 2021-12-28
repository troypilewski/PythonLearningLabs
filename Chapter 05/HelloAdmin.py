# users = ['mike', 'hayden', 'tyler', 'kim', 'mark', 'admin']
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello, {}. Would you like to view a status report?".format(user))
        else:
            print("Hello, {}. What would you like to do today?".format(user.title()))
else:
    print("There are no users signed up.")
