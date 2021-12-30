prompt = "\nEnter 'quit' to end the program."
prompt += "\nEnter a message and I will repeat it back to you: "

active = True

while active:

    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print("\n{}".format(message))