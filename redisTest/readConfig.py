import os
import configparser

proDir=os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(proDir,'pytest.ini')

class ReadConfig:
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)
    def get_http(self, name):
        return self.cf.get('HTTP',name)