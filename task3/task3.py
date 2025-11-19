import json
import sys

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

    if len(sys.argv) < 4:
        print("Ошибка! Нужно передать 3 аргумента: values.json tests.json report.json")
        return

    path_values = sys.argv[1]
    path_tests = sys.argv[2]
    path_report = sys.argv[3]

    values_json = get_json(path_values)
    tests_json = get_json(path_tests)

    values_map = get_values_map(values_json)

    if 'tests' in tests_json:
        put_values(tests_json['tests'], values_map)

    with open(path_report, "w", encoding='utf-8') as f:
        json.dump(tests_json, f, indent=2, ensure_ascii=False)
    print(f"Результат успешно записан в файл: {path_report}")

main()