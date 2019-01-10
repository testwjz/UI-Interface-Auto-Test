import os
import configparser

dirpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

class ReadConfig:
    def __init__(self, configPath):
        self.cf = configparser.ConfigParser()
        self.cf.read_file(open(configPath,encoding="utf-8"))

    def get(self, name, data):
        return self.cf.get(name, data)
