import logging

import glitch.api.Connector as Connector

logger = logging.getLogger(__name__)

FIREBASE_KEY = "eIoqQtmkAQI:APA91bG0UJLCfZrWvqNTvcH-TJUNpTE-oVHdSUUL7VGF0LaE86tNr" \
               "-FYFpY6hyj6u0DDer8Dr7vCfF2WO5jP248oIU_xBf2kW4mnIgJ5GzYjqrnEhfIVDKk2Jn_ru1YO4v80jdKC1vvA"
APP_VERSION = '1.30'


class User:
    """Store user information."""

    def __init__(self):
        self.UserID = 0
        self.Username = ""
        self.Role = ""
        self.IP = ""
        self.Rank = 0
        self.Money = 0
        self.Premium = 0
        self.IsPremium = 0
        self.PremiumRemaining = ""
        self.ProfileImage = ""
        self.BruteForce = 0
        self.Rootkit = 0
        self.ZeroDay = 0
        self.DDOS = 0
        self.Firewall = 0
        self.IPS = 0
        self.HDS = 0
        self.VPN = 0
        self.SDK = 0
        self.Scan = 0
        self.Antivirus = 0
        self.RAM = 0
        self.Keylogger = 0
        self.Cryptography = 0
        self.Reputation = 0
        self.Status = ""
        self.SkinPrimary = ""
        self.SkinSecondary = ""
        # custom variable
        self.Password = ""
        self.Encrypted = ""
        self.SessionKey = ""
        self.Email = ""
        self.FirebaseKey = ""

    # main function
    def get_user_info(self):
        response = Connector.post_request("/User/GetUserInfo",
                                          Username=self.Username,
                                          SessionKey=self.SessionKey,
                                          AppVersion=APP_VERSION)
        if response != "":
            try:
                r = response.json()
                self.UserID = r['UserID']
                self.Username = r['Username']
                self.Role = r['Role']
                self.IP = r['IP']
                self.Rank = int(r['Rank'])
                self.Money = int(r['Money'])
                self.Premium = int(r['Premium'])
                self.IsPremium = True if r['IsPremium'] == "TRUE" else False
                self.PremiumRemaining = int(r['PremiumRemaining'])
                self.ProfileImage = r['ProfileImage']
                self.BruteForce = int(r['BruteForce'])
                self.Rootkit = int(r['Rootkit'])
                self.ZeroDay = int(r['ZeroDay'])
                self.DDOS = int(r['DDOS'])
                self.Firewall = int(r['Firewall'])
                self.IPS = int(r['IPS'])
                self.HDS = int(r['HDS'])
                self.VPN = int(r['VPN'])
                self.SDK = int(r['SDK'])
                self.Scan = int(r['Scan'])
                self.Antivirus = int(r['Antivirus'])
                self.RAM = int(r['RAM'])
                self.Keylogger = int(r['Keylogger'])
                self.Cryptography = int(r['Cryptography'])
                self.Reputation = int(r['Reputation'])
                self.Status = r['Status']
                self.SkinPrimary = r['SkinPrimary']
                self.SkinSecondary = r['SkinSecondary']
            except ValueError:
                print(response.text)
                print('getuserinfo')
                exit(4)
        return

    def encrypt_password(self):
        response = Connector.post_request("/Misc/Encryption",
                                          Input=self.Password)
        if response != "":
            self.Encrypted = response.text
        return

    def login(self):
        response = Connector.post_request("/User/Login",
                                          Username=self.Username,
                                          Password=self.Encrypted)
        if response != "Incorrect username or password." and response != "Error!" and response != "":
            self.SessionKey = response.text
        else:
            logger.error(response)
            exit(0)
        return

    def verify_session(self):
        response = Connector.post_request("/User/VerifySession",
                                          Username=self.Username,
                                          SessionKey=self.SessionKey)
        if response != "":
            if response.text == "TRUE":
                return True
        return False

    def get_theme_colors(self):
        response = Connector.post_request("/User/GetThemeColors",
                                          Username=self.Username,
                                          SessionKey=self.SessionKey)
        if response != "":
            try:
                r = response.json()
                self.SkinPrimary = r['Primary']
                self.SkinSecondary = r['Secondary']
            except ValueError:
                print(response.text)
        return

    def check_new(self):
        response = Connector.post_request("/User/CheckNew",
                                          Username=self.Username,
                                          SessionKey=self.SessionKey)
        if response != "":
            if response.text == "0":
                return False
            elif response.text == "1":
                return True
        return False

    def update_firebase(self):
        response = Connector.post_request("/User/UpdateFirebase",
                                          Username=self.Username,
                                          SessionKey=self.SessionKey,
                                          FirebaseKey=FIREBASE_KEY)
        if response != "":
            if response.text == "TRUE":
                return True
        return False
