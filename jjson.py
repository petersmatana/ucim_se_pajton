# -*- coding: utf-8 -*-

import json
from json import dumps
from json import loads

# oneJson = '{["jedna hodnota"]}'
# j1 = json.loads(oneJson)

def json_data():
    jsonData = '{"klic": true, "klic2": {"vnoreni": 132}, ' \
               '"asd": ["w", "a", "c"], "asd": null}'
    jsonToPython = json.loads(jsonData)
    print 'json = ', jsonToPython


def py_dict():
    pyDict = {'klic': 'hodnota', 'klic2': 100, 'klic3': None}
    dictToPy = json.dumps(pyDict)
    print 'python dict = ', dictToPy
