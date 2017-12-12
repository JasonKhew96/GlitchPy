import glitch.api.Connector as Connector


class Remote:
    def __init__(self):
        return

    @staticmethod
    def get_ips(username, sessionkey):
        response = Connector.post_request("/Remote/GetIPs", Username=username, SessionKey=sessionkey)
        if response != "":
            try:
                r = response.json()
                return r
            except ValueError:
                return ""
        return ""

    @staticmethod
    def scan_ip(username, sessionkey, target):
        response = Connector.post_request("/Remote/ScanIP", Username=username, SessionKey=sessionkey, Target=target)
        if response != "":
            try:
                r = response.json()
                return r
            except ValueError:
                return ""
        return ""
