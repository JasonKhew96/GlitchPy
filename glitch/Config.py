import json
import os
from configparser import ConfigParser

configfile_name = "config.ini"


def is_config_new():
    # Check if there is already a configuration file
    if not os.path.isfile(configfile_name):
        # Create the configuration file as it doesn't exist yet
        cfgfile = open(configfile_name, 'w')

        # Add content to the file
        config = ConfigParser()
        config.add_section('user')
        config.set('user', 'username', '')
        config.set('user', 'password', '')
        config.set('user', 'upgrade', '["BruteForce", "Rootkit", "ZeroDay", "DDOS", "Firewall", "IPS", "HDS", "VPN", '
                                      '"SDK", "Scan", "Antivirus", "RAM", "Keylogger", "Cryptography", "Bank", '
                                      '"Spyware", "Adware"]')
        config.set('user', 'session_key', '')
        config.write(cfgfile)
        cfgfile.close()
        return False
    return True


def get_config(section, key):
    config = ConfigParser()
    config.read(configfile_name, 'UTF-8')
    return config.get(section, key)


def is_session_key_exist():
    ret = True if get_config('user', 'session_key') != '' else False
    return ret


def is_valid():
    if (get_config('user', 'username') != "") and (get_config('user', 'username') != ""):
        return True
    else:
        return False


def get_username():
    return get_config('user', 'username')


def get_password():
    return get_config('user', 'password')


def get_upgrade():
    return json.loads(get_config('user', 'upgrade'))


def get_session_key():
    return get_config('user', 'session_key')
