def ready_event(channel, link):
    print("Listening to "+channel+" at "+link)
 
def error_event(error):
    print(error) # Prints the error if one is received

def message_event(msg): # This event fires whenever there is a new message in chat
    author = msg[0] # msg[0] is the message author
    content = msg[1] # msg[1] is the message content
    id = msg[2] # msg[2] is the message id
    
    print(author+": "+content) # Prints new chat messages