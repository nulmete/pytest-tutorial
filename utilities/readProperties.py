import configparser
import os


class ReadConfig:
    config = configparser.RawConfigParser()
    config.read(os.path.join(os.getcwd(), 'Configurations/config.ini'))

    @classmethod
    def get_url(cls):
        url = cls.config.get("common2", "baseURL")
        return url

    @classmethod
    def get_username(cls):
        username = cls.config.get("common2", "username")
        return username

    @classmethod
    def get_password(cls):
        password = cls.config.get("common2", "password")
        return password