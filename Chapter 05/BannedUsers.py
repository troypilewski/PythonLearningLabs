bannedUsers = ['marie', 'andrew', 'pov']
user = 'troy'

if user not in bannedUsers:
    print("{}, you may respond to the post.".format(user.title()))
else:
    print("{}, you are banned from posting on the forum.".format(user.title()))
