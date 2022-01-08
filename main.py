import requests
import json
import os.path

csgo_folder = "F:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/csgo/cfg"
config_site = "https://pastebin.com/raw/G8ALVzXe"
name_of_config = 'sumss.cfg'

# Get config from site
config_request = requests.get(config_site)

# Save config to file 
with open(os.path.join(csgo_folder, name_of_config), 'w') as config_file:
    config_file.write(config_request.text.replace('\n', ''))