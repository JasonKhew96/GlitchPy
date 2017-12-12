import glitch.api.Connector as Connector


class Items:
    def __init__(self):
        return

    @staticmethod
    def get_active(username, sessionkey):
        Connector.post_request("/Items/GetActive", Username=username, SessionKey=sessionkey)
        return
