import json
import threading


def parse_and_print_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print(f"Data from {file_name}:")
        print(json.dumps(data, indent=4))


file_names = ['json_file_1.json', 'json_file_2.json']
threads = []

for file_name in file_names:
    thread = threading.Thread(target=parse_and_print_json, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
