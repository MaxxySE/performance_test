import json


def get_json(filename):
    with open(filename) as f:
        js = json.load(f)

    return js

def get_values_map(values_json):
    values_map = {}

    for entry in values_json['values']:
        values_map[entry['id']] = entry['value']
    return values_map

def put_values(tests_list, values_map):

    for test in tests_list:
        if test['id'] in values_map:
            test['value'] = values_map[test['id']]

        if 'values' in test:
            put_values(test['values'], values_map)

def main():
    values_json = get_json("values.json")
    tests_json = get_json("tests.json")

    values_map = get_values_map(values_json)

    if 'tests' in tests_json:
        put_values(tests_json['tests'], values_map)


    print(tests_json)

main()