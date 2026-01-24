## chat.py
## method to get data from stdin
## method to print to screen
import communication
import sys

# Codes for styles/colors
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RED = '\033[31m'
RESET = '\033[0m'

## Receive Message Function
def LauraMaxwell(comon_sivan):
    for message in comon_sivan[0]:
        print(f'{BOLD}{BLUE}{"[" + message["user"] + "]"}: {YELLOW}{message["message"]}{RESET}')

channel = 'chat'
communication.startStream(channel, LauraMaxwell)

# print welcome message
print(f'{BOLD}{GREEN}Welcome to the chat!\nEnter your user: {YELLOW}')

# Ask for user once
user = input(f'{BOLD}{BLUE}User: {YELLOW}')

## Send Message Function
while True:
    
    message = input(f'{BOLD}{BLUE}Message: {YELLOW}')
    payload = {"user": user, "message": message}

    # if user types logout, they should be logget out, just them by updating the running flag
    if message == 'logout':
        payload = {"user": f"{RED}SYSTEM", "message": f"{user} has left the chat"}
        communication.send(channel, payload)
        communication.update_running(False)
        sys.exit() 

    communication.send(channel, payload)

    
