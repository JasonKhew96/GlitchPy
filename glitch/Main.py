import logging
from operator import itemgetter
from random import randint
from time import sleep

from glitch.Config import is_config_new, is_session_key_exist, is_valid, get_username, get_password, get_session_key, \
    get_upgrade
from glitch.api.Attack import Attack
from glitch.api.Bank import Bank
from glitch.api.Items import Items
from glitch.api.Misc import get_package_list
from glitch.api.Remote import Remote
from glitch.api.Software import Software
from glitch.api.Tournaments import Tournaments
from glitch.api.User import User

user = User()
bank = Bank()
items = Items()
tournaments = Tournaments()
remote = Remote()
attack = Attack()
software = Software()

logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s [%(threadName)10s][%(module)9s][%(levelname)5s] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


def check():
    logger.info('checking...')
    if not is_config_new():
        logger.warning("Configuration file generated. Please set your username and password.")
        exit(0)
    if not is_valid():
        logger.warning("Configuration not set!")
        exit(0)


def simulate_login():
    logger.info('logging in!!.')
    if not is_session_key_exist():
        get_package_list()
        sleep(randint(10, 20))
        user.Username = get_username()
        user.Password = get_password()
        user.encrypt_password()
        user.login()
        user.update_firebase()
    else:
        sleep(randint(3, 8))
        user.Username = get_username()
        user.Password = get_password()
        user.SessionKey = get_session_key()

    user.get_theme_colors()
    user.get_user_info()
    user.check_new()
    user.get_theme_colors()
    user.get_user_info()
    bank.get_bank_info(user.Username, user.SessionKey)
    tournaments.get_status(user.Username, user.SessionKey)
    items.get_active(user.Username, user.SessionKey)
    return


def attack_ip(count=randint(1, 3)):
    sleep(randint(3, 8))
    logger.info('Init Hacking console!')
    user.get_theme_colors()
    user.get_theme_colors()
    user.get_user_info()
    user.get_user_info()
    for x in range(0, count):
        ips = remote.get_ips(user.Username, user.SessionKey)
        for ip in ips:
            sleep(randint(3, 8))
            if ip['CanAttack'] == 'TRUE':
                scanip = remote.scan_ip(user.Username, user.SessionKey, ip['IP'])
                message = '\n'
                message += '-------------------------------------------\n'
                message += 'IP:        {:>15}\n'.format(scanip['IP'])
                message += 'Money:     {:>15}$\n'.format(scanip['Money'])
                message += 'MinerCash: {:>15}$\n'.format(scanip['MinerCash'])
                message += 'Firewall: {:>4}  Antivirus:    {:>4}\n'.format(scanip['Firewall'],
                                                                           scanip['Antivirus'])
                message += 'IPS:      {:>4}  Cryptography: {:>4}\n'.format(scanip['IPS'],
                                                                           scanip['Cryptography'])
                message += 'HDS:      {:>4}\n'.format(scanip['HDS'])
                message += 'BruteForceChance: {:>3}   UserBruteForce: {:>3}\n'.format(scanip['BruteForceChance'],
                                                                                      scanip['UserBruteForce'])
                message += 'RootkitChance:    {:>3}   UserRootkit:    {:>3}\n'.format(scanip['RootkitChance'],
                                                                                      scanip['UserRootkit'])
                message += 'ZeroDayChance:    {:>3}   UserZeroDay:    {:>3}\n'.format(scanip['ZeroDayChance'],
                                                                                      scanip['UserZeroDay'])
                message += '-------------------------------------------'
                logger.info(message)
                sleep(randint(3, 8))
                if int(scanip['BruteForceChance']) >= 75:
                    logger.info('Attacking: ' + ip['Username'])
                    attack.brute_force_attack(user.Username, user.SessionKey, ip['Username'])
                else:
                    logger.info('BruteForce percent too low... {}%'.format(scanip['BruteForceChance']))
        sleep(randint(3, 8))
    return


def software_upgrade():
    sleep(randint(3, 8))
    logger.info('Checking for software to upgrade...')
    user.get_theme_colors()
    if not user.verify_session():
        logger.warning('Session expired...')
        exit(0)
    user.get_user_info()
    software.get_software_levels(user.Username, user.SessionKey)
    user.get_theme_colors()
    sleep(randint(3, 8))
    # upgrade_list = ['BruteForce', 'Rootkit', 'ZeroDay', 'DDOS', 'Firewall', 'IPS', 'HDS', 'VPN', 'SDK', 'Scan',
    #                 'Antivirus', 'RAM', 'Keylogger', 'Cryptography', 'Bank', 'Spyware', 'Adware']
    upgrade_list = get_upgrade()
    while True:
        data_list = list()
        for x in upgrade_list:
            level, upgrade1, upgrade5, upgrade10 = software.software_split(software.software_dict[x])
            data_list.append([x, level, upgrade1, upgrade5, upgrade10])
        data_list.sort(key=itemgetter(1), reverse=False)
        logger.debug(data_list)

        logger.info('checking upgrade cost...')
        logger.debug('{}\nMoney: {}, {}, {}, {}'.format(data_list[0][0], software.software_dict['Money'],
                                                        data_list[0][4], data_list[0][3], data_list[0][2]))
        if data_list[0][4] <= software.software_dict['Money']:
            logger.info('Upgrade 10: ' + data_list[0][0])
            software.upgrade_software(user.Username, user.SessionKey, data_list[0][0], '10')
        elif data_list[0][3] <= software.software_dict['Money']:
            logger.info('Upgrade 5: ' + data_list[0][0])
            software.upgrade_software(user.Username, user.SessionKey, data_list[0][0], '5')
        elif data_list[0][2] <= software.software_dict['Money']:
            logger.info('Upgrade 1: ' + data_list[0][0])
            software.upgrade_software(user.Username, user.SessionKey, data_list[0][0], '1')
        else:
            sleep(randint(3, 8))
            return
        software.get_software_levels(user.Username, user.SessionKey)
        user.get_user_info()

        sleep(randint(3, 8))


def main():
    check()
    simulate_login()
    try:
        while True:
            software_upgrade()
            attack_ip()
    except KeyboardInterrupt:
        logger.warning('Exiting...')
    return


if __name__ == "__main__":
    main()
