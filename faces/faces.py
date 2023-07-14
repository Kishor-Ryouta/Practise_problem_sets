#user input
x = input('Enter your greeting message: ').strip()

#conveting emoticons to emojis
emoji = x.replace(":)","🙂").replace(":(", "🙁")

print(emoji)

