def message_event(msg): # This event fires whenever there is a new message in chat
    author = msg[0] # msg[0] is the message author
    content = msg[1] # msg[1] is the message content
    
    print(author+": "+content) # Prints new chat messages