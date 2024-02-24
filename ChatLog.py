# Opens Folder That stores the AI Responses
from Voice import SpeakText


Chats = "AIResponce.txt"

def chatlogs():
    with open(Chats, 'r') as file:
    # Read the contents of the file
        chat = file.read()
        file.close()
    
    return chat

def closeDownTXT():
    with open(Chats, "w") as file:
        file.write("notepad")

# print(AiResponces)