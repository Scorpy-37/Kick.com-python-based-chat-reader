def ready_event(channel, link):                # This event fires whenever the script fully launches
    print("Listening to "+channel+" at "+link) # Print the channel and link the script is listening to
    history = retrieve_past()                  # Retrieves the messages sent before this script was launched
    change_interval(0.05)                      # Changes the script run interval to every 0.05 seconds, not required to be set
    
    #username = "login username" # Assign the username of the bot
    #password = "login password" # Assign the password of the bot, make sure to use a seperate file for this so you don't accidentally leak your password!
    #login(username, password)   # Log into the bots account, make sure the window is maximized while logging in
    # Read README.txt to learn how to use login and send_message

def message_event(msg): # This event fires whenever there is a new message in chat
    author = msg[0]     # msg[0] is the message author
    content = msg[1]    # msg[1] is the message content
    message_id = msg[2] # msg[2] is the message id
    user_id = msg[3]    # msg[3] is the user id
    
    print(author+": "+content)      # Prints new chat messages
    #print(user_id+": "+message_id) # Prints new chat message ids
    
    #if str.lower(content) == "hi": # Check for a specific message
    #    send_message("Hello!")     # Send a message in chat (only works if logged in)