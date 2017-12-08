import pprint
import json

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:        
        data = json.loads(data_file.read())

except OSError:
    print("Файл не найден! Файл должен называться: {}".format(filename))


pprint.pprint(data)
