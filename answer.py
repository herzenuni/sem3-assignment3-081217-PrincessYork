import pprint
import json

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:        
        data = json.loads(data_file.read())

except OSError:
    print("Файл не найден! Файл должен называться: {}".format(filename))


pprint.pprint(data)

# Вывести company email phone address
for index, i in enumerate(data):
	obj = {}
	obj.update(
			{
				'company' : i.get('company'),
				'email' : i.get('email'),
				'phone' : i.get('phone'),
				'address' : i.get('address')
			}
		)

	print("\nIndex", index)
	pprint.pprint(obj)
