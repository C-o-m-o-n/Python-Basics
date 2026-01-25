## chat.py
## Simple chat client with commands support
import communication
import sys
from datetime import datetime

# Colors for terminal
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RED = '\033[31m'
CYAN = '\033[36m'
RESET = '\033[0m'

# Store the current username
current_user = ""
channel = 'chat'

def format_time():
    """Return current time as HH:MM"""
    return datetime.now().strftime("%H:%M")

def show_history(count=10):
    """Display message history"""
    print(f"\n{YELLOW}--- Last {count} Messages ---{RESET}")
    history = communication.getHistory(channel, count)
    if history:
        for msg in history:
            if isinstance(msg, dict):
                user = msg.get("user", "Unknown")
                text = msg.get("message", "")
                if "SYSTEM" in user:
                    print(f"{YELLOW}⚡ {text}{RESET}")
                else:
                    print(f"{CYAN}← [{user}]: {text}{RESET}")
    else:
        print(f"{CYAN}No message history yet.{RESET}")
    print(f"{YELLOW}--- End of History ---{RESET}\n")

def show_help():
    """Display available commands"""
    print(f"""
{YELLOW}╔══════════════════════════════════════╗
║           Available Commands          ║
╠══════════════════════════════════════╣
║  {CYAN}/help{YELLOW}      - Show this help message  ║
║  {CYAN}/history{YELLOW}   - Show last 10 messages   ║
║  {CYAN}/history N{YELLOW} - Show last N messages    ║
║  {CYAN}/clear{YELLOW}     - Clear the screen        ║
║  {CYAN}/logout{YELLOW}    - Leave the chat          ║
╚══════════════════════════════════════╝{RESET}
""")

def clear_screen():
    """Clear the terminal screen"""
    print('\033[2J\033[H', end='')

def handle_command(command):
    """Process a command and return True if handled, False otherwise"""
    parts = command[1:].split()  # Remove the / and split
    cmd = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    if cmd == "help":
        show_help()
        return True
    
    elif cmd == "history":
        count = 10
        if args:
            try:
                count = int(args[0])
            except ValueError:
                print(f"{RED}Invalid number. Using default (10).{RESET}")
        show_history(count)
        return True
    
    elif cmd == "clear":
        clear_screen()
        return True
    
    elif cmd == "logout":
        leave_msg = {"user": "SYSTEM", "message": f"{current_user} has left"}
        communication.send(channel, leave_msg)
        communication.update_running(False)
        print(f"{GREEN}Goodbye! 👋{RESET}")
        sys.exit()
    
    else:
        print(f"{RED}Unknown command: /{cmd}. Type /help for available commands.{RESET}")
        return True

def on_message_received(data):
    """Handle incoming messages"""
    for msg in data[0]:
        if not isinstance(msg, dict):
            continue
        
        user = msg.get("user", "")
        text = msg.get("message", "")
        time_str = format_time()
        
        # Skip our own messages
        if user == current_user:
            continue
        
        if "SYSTEM" in user:
            print(f"\n{YELLOW}[{time_str}] ⚡ {text}{RESET}")
        else:
            print(f"\n{CYAN}[{time_str}] ← [{user}]: {text}{RESET}")

# === MAIN PROGRAM ===

# Welcome and get username
print(f"{BOLD}{GREEN}Welcome to Chat!{RESET}")
current_user = input(f"{BLUE}Username: {YELLOW}").strip()

if not current_user:
    current_user = "Anonymous"

print(f"{GREEN}Joined as {current_user}. Type /help for commands.{RESET}\n")

# Start listening for messages
communication.startStream(channel, on_message_received)

# Announce that we joined
join_msg = {"user": "SYSTEM", "message": f"{current_user} has joined"}
communication.send(channel, join_msg)

# Main loop
while True:
    message = input(f"{BLUE}> {RESET}").strip()
    
    if not message:
        continue
    
    # Check if it's a command
    if message.startswith('/'):
        handle_command(message)
        continue
    
    # Send the message
    payload = {"user": current_user, "message": message}
    communication.send(channel, payload)
    
    time_str = format_time()
    print(f"{GREEN}[{time_str}] → {message}{RESET}")
