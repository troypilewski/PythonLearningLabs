favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# for name, language in favorite_languages.items():
#     print("{}'s favorite languaage is {}.".format(name.title(), language.title()))

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print("\t{}, I see you love {}.".format(name.title(), language))

for name, languages in favorite_languages.items():
    print("\n{}'s favorite langauges are:".format(name.title()))
    for language in languages:
        print("\t{}".format(language.title()))