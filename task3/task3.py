import json


def get_json(filename):
    with open(filename) as f:
        js = json.load(f)

    return js

values_json = get_json("values.json")
tests_json = get_json("tests.json")

def get_values():
    values_map = {}

    for entry in values_json['values']:
        values_map[entry['id']] = entry['value']
    return values_map

def put_values(values_map):
    for entry in tests_json['tests']:
        print(entry)

put_values(get_values())

get_values()
#print(get_json("values.json")['values'])
#print(get_json("tests.json"))