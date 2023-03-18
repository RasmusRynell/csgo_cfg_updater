import requests
import json
import os.path
import sys
import difflib
import argparse

def __colored(text, color):
    if color == "red":
        return "\033[1;31m" + text + "\033[0m"
    elif color == "green":
        return "\033[1;32m" + text + "\033[0m"
    return text


def __get_config_from_site(config_site):
    config_request = requests.get(config_site)
    if config_request.status_code != 200:
        raise Exception("Config site not found")
    if config_request.text == "":
        raise Exception("Found to config at " + config_site)
    return config_request.text


def __get_config_from_folder(folder, name):
    if not os.path.isdir(folder):
        raise Exception("Config folder not found at " + folder)
    if not os.path.isfile(os.path.join(folder, name)):
        print("WARNING: Config file not found at " + os.path.join(folder, name), flush=True)
        return ""
    with open(os.path.join(folder, name), 'r', encoding="utf8") as f:
        return f.read()


def __print_changes(config_text, current_config_text):
    if config_text == current_config_text:
        print('No changes', flush=True)
        return

    for line in difflib.unified_diff(current_config_text.splitlines(), config_text.splitlines(), lineterm=''):
        if line.startswith('-'):
            print(__colored(line, 'red'), flush=True)
        elif line.startswith('+'):
            print(__colored(line, 'green'), flush=True)
        else:
            print(line)


def __save_config(path, text):
    with open(path, 'w', newline='', encoding='utf-8') as config_file:
        config_file.write(text)
        print("Wrote to file: " + path, flush=True)



def main(config_folder, config_site, name_of_config, write_to_auto_exec, print_changes):
    print("Starting", flush=True)
    print("Config path: " + config_folder, flush=True)
    print("Config site: " + config_site, flush=True)
    print("Config name: " + name_of_config, flush=True)
    print("Write to autoexec: " + str(write_to_auto_exec), flush=True)
    print("Print changes: " + str(print_changes), flush=True)

    config_text = __get_config_from_site(config_site)
    current_config_text = __get_config_from_folder(config_folder, name_of_config)

    if print_changes:
        __print_changes(config_text, current_config_text)

    __save_config(os.path.join(config_folder, name_of_config), config_text)

    if write_to_auto_exec:
        __save_config(os.path.join(config_folder, 'autoexec.cfg'), config_text)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update your csgo config.')

    parser.add_argument('Config_path', metavar='Config_path', type=str,
                    help='Path to your csgo config folder')

    parser.add_argument('Config_site', metavar='Config_site', type=str,
                    help='Website where your config is located (has to be raw text such as pastebin or GIST)')
    
    parser.add_argument('Config_name', metavar='Config_name', type=str,
                    help='Name of your config file')

    parser.add_argument('--write_to_auto_exec', metavar='write_to_auto_exec', type=bool, default=True,
                    help='Write to autoexec.cfg')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print changes')
                    

    args = parser.parse_args()
    main(args.Config_path, args.Config_site, args.Config_name, args.write_to_auto_exec, args.verbose)
    
