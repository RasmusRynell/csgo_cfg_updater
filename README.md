# Update csgo config

positional arguments:
  Config_path           Path to your csgo config folder (example:  <steam_path>/steamapps/common/Counter-Strike Global Offensive/csgo/cfg)
  Config_site           Website where your config is located (has to be raw text such as pastebin or GIST) (example: https://pastebin.com/raw/...)
  Config_name           Name of your config file (example: example.cfg)

options:
  -h, --help            show this help message and exit
  --write_to_auto_exec  write_to_auto_exec (default: True)
                        Write to autoexec.cfg
  -v, --verbose         Print changes

Example:
python3 update_config.py "<Config_site>" "<Config_path>" "<Config_name>" --verbose