import logging
import re

import glitch.api.Connector as Connector

logger = logging.getLogger(__name__)


class Software:
    def __init__(self):
        self.software_dict = dict()

    def get_software_levels(self, username, sessionkey):
        response = Connector.post_request('/Software/GetSoftwareLevels', Username=username, SessionKey=sessionkey)
        if response != "":
            try:
                r = response.json()
                self.software_dict['Money'] = int(r['Money'].replace('$', '').replace(',', ''))
                self.software_dict['BruteForce'] = r['BruteForce']
                self.software_dict['Rootkit'] = r['Rootkit']
                self.software_dict['ZeroDay'] = r['ZeroDay']
                self.software_dict['DDOS'] = r['DDOS']
                self.software_dict['Firewall'] = r['Firewall']
                self.software_dict['IPS'] = r['IPS']
                self.software_dict['HDS'] = r['HDS']
                self.software_dict['VPN'] = r['VPN']
                self.software_dict['SDK'] = r['SDK']
                self.software_dict['Scan'] = r['Scan']
                self.software_dict['Antivirus'] = r['Antivirus']
                self.software_dict['RAM'] = r['RAM']
                self.software_dict['Keylogger'] = r['Keylogger']
                self.software_dict['Cryptography'] = r['Cryptography']
                self.software_dict['Bank'] = r['Bank']
                self.software_dict['Spyware'] = r['Spyware']
                self.software_dict['Adware'] = r['Adware']
            except ValueError:
                logger.error(response.text)
                exit(0)
        return

    def upgrade_software(self, username, sessionkey, software, upgradeby):
        response = Connector.post_request('/Software/UpgradeSoftware',
                                          Username=username,
                                          SessionKey=sessionkey,
                                          Software=software,
                                          UpgradeBy=upgradeby)
        if response != '':
            try:
                r = response.json()
                self.software_dict['Money'] = int(r['NewCash'])
            except KeyError:
                logger.error(response.text)
                exit(0)
        return

    @staticmethod
    def software_split(software):
        reg = re.compile('\((.*)\)&1\[\$(.*)\]&5\[\$(.*)\]&10\[\$(.*)\]')
        try:
            match = reg.match(software)
            level = int(match.group(1))
            upgrade1 = int(match.group(2).replace(',', ''))
            upgrade5 = int(match.group(3).replace(',', ''))
            upgrade10 = int(match.group(4).replace(',', ''))
            return level, upgrade1, upgrade5, upgrade10
        except AttributeError:
            logger.error('software_split')
            return 0, 0, 0, 0
        except Exception as e:
            logger.error('Unknown exception: {}'.format(e))
            exit(0)
