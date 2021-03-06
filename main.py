import requests
import json
import os.path
import sys
import time
import datetime
import difflib

def colored(text, color):
    if color == "red":
        return "\033[1;31m" + text + "\033[0m"
    elif color == "green":
        return "\033[1;32m" + text + "\033[0m"
    elif color == "yellow":
        return "\033[1;33m" + text + "\033[0m"
    elif color == "blue":
        return "\033[1;34m" + text + "\033[0m"
    elif color == "magenta":
        return "\033[1;35m" + text + "\033[0m"
    elif color == "cyan":
        return "\033[1;36m" + text + "\033[0m"
    elif color == "white":
        return "\033[1;37m" + text + "\033[0m"
    else:
        return text



csgo_folder = "F:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/csgo/cfg"
config_site = "https://pastebin.com/raw/G8ALVzXe"
name_of_config = 'sumss.cfg'

# Get config from site
config_request = requests.get(config_site)

# Get current config from csgo_filder if name_of_config exists
if os.path.isfile(csgo_folder + '/' + name_of_config):
    with open(csgo_folder + '/' + name_of_config, 'r') as f:
        current_config = f.read()

# Check if config is different from current config
text = config_request.text.replace('\n', '')

if text.splitlines() != current_config.splitlines():
    # Print the difference, removed text lines in red and added lines in green
    for line in difflib.unified_diff(current_config.splitlines(), text.splitlines(), lineterm=''):
        if line.startswith('-'):
            print(colored(line, 'red'), flush=True)
        elif line.startswith('+'):
            print(colored(line, 'green'), flush=True)
        else:
            print(line)
else:
    print('No changes', flush=True)


# Save config to file
with open(os.path.join(csgo_folder, name_of_config), 'w') as config_file:
    config_file.write(text)