prompt = "If you tell me your full name, I can personalize a message to you."
prompt += "\nWhat is your full name? "

message = input(prompt)

print("\nHello, {}.".format(message))