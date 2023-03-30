def message_event(msg):
    author = msg[0] # msg[0] is the message author
    content = msg[1] # msg[1] is the message content
    print(author+": "+content) # remove this if you'd like
    
    # your code here

exec(open("reader.py").read()) # DO NOT REMOVE THIS, this line runs the page reader