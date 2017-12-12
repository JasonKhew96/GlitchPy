import logging

import glitch.api.Connector as Connector

logger = logging.getLogger(__name__)


class Tournaments:
    def __init__(self):
        self.Type = 0
        self.Rank = ""

    def get_status(self, username, sessionkey):
        response = Connector.post_request("/Tournaments/GetStatus", Username=username, SessionKey=sessionkey)
        if response != "":
            try:
                r = response.json()
                self.Type = int(r['Type'])
                self.Rank = r['Rank']
            except ValueError:
                logger.error(response.text)
        return
