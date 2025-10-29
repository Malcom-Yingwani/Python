simon_says = ["jump", "touch your nose", "roll over", " one-two"]
sent_messages = []

def show_messages(list):
    """Prints each message in a list"""
    
    while simon_says:
        saying = simon_says.pop()
        print(f"Simon says {saying}.")
        sent_messages.append(saying)

show_messages(simon_says)

print(simon_says)
print(sent_messages)