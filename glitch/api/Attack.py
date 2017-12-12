import logging

import glitch.api.Connector as Connector

logger = logging.getLogger(__name__)


class Attack:
    def __int__(self):
        return

    @staticmethod
    def brute_force_attack(username, sessionkey, target):
        response = Connector.post_request("/Attack/BruteForceAttack",
                                          System="Brute Force",
                                          Username=username,
                                          SessionKey=sessionkey,
                                          Target=target)
        if response != "":
            logger.info(response.text)
        return
