def getFormattedName(firstName, lastName):
    """Return formatted Full Name"""
    fullName = "{} {}".format(firstName, lastName)
    return fullName.title()

musician = getFormattedName('jimi', 'hendrix')
print(musician)