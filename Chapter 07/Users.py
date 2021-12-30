unconfirmed = ['alice', 'brian', 'candace']
confirmed = []

while unconfirmed:
    currentUser = unconfirmed.pop()

    print("Verifing: {}".format(currentUser.title()))
    confirmed.append(currentUser)

print("\nThe following user have been confirmed:")
for user in confirmed:
    print("{}".format(user.title()))
