import logging

import glitch.api.Connector as Connector

logger = logging.getLogger(__name__)


class Bank:
    """Store bank information."""

    def __init__(self):
        self.Money = 0
        self.BankValue = 0
        self.Premium = 0

    def get_bank_info(self, username, sessionkey):
        response = Connector.post_request("/Bank/GetBankInfo", Username=username, SessionKey=sessionkey)
        if response != "":
            try:
                r = response.json()
                self.Money = int(r['Money'])
                self.BankValue = int(r['BankValue'])
                self.Premium = int(r['Premium'])
            except ValueError:
                logger.info(response.text)
        return
