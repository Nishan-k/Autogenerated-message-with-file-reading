import datetime

#  TODO 1: Create a common message for everyone:
with open("message_blueprint.txt", mode="w") as file:
    file.write("Hello name, \n\nI want to invite you to an event happening on date. \nPlease feel free to join us.\n\n"
               "Kind regards, \nNishan Karki")

# TODO 2: Create the names of the partcipants:

with open("participants.txt", mode="w") as file:
    file.write("Naruto,\nSasuke,\nGaara,\nKakashi,\nRock-Lee,\nMinato,\nHinata,\nJiraiya")

# TODO 3: Make a list of messages for each participants ready to be sent:

with open("participants.txt", mode='r') as file:
    contents = file.read()
    participants = contents.split(',')
    participants = [p.replace("\n", '') for p in participants]

for name in participants:
    with open(f"./messages_ready_to_send/letter_for_{name}.txt", mode='w') as letter:
        with open("message_blueprint.txt", mode="r") as message:
            content = message.read()
        content = content.replace('name', name)
        content = content.replace('date', str(datetime.datetime.now().date()))
        letter.write(content)
