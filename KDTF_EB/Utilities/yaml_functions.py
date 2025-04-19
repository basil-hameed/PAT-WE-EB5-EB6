"""
This file contains all the yaml functions
"""

from yaml import load
from yaml.loader import SafeLoader

class YAMLReader:

    def __init__(self, file_name):
        self.file = file_name

    # reader method to simply read the data
    def reader(self):
        with open(self.file) as file:
            data = load(file, Loader=SafeLoader)
            return data