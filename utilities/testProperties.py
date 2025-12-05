import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def GetEmail():
        username = config.get('commonInfo', 'email')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('commonInfo', 'password')
        return password

