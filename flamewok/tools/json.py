#! /usr/bin/env python3

import json
import os

"""
Simple json file loader / saver

Example:

json_data = JsonFile('data.json')

data = {
    'app1': {'folder': 'here', 'desktop': 'here'},
    'app2': {'folder': 'there', 'desktop': 'by there'}
}


json_data.save(data)
data = json_data.load()
data['app3'] = {'folder': 'new folder', 'desktop': 'somewhere'}
json_data.save(data)
results = json_data.load()
print(results)
"""


class JsonFile:
    """Interface with a json file"""

    def __init__(self, file_path):
        self.file = file_path

    def save(self, data):
        with open(self.file, 'w') as file:
            json.dump(data, file)

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as file:
                data = json.load(file)
            return data
        else:
            return []
