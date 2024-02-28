import json
import argparse
import os
import itertools

parser = argparse.ArgumentParser(description='Provide the Json File name')
parser.add_argument('filename', type=str, help='Provide the filename containing json objects')
args = parser.parse_args()

with open(args.filename, 'r') as file:
    orders_data = json.load(file)

for order in orders_data:
    file_path = "customers.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            customers_data = json.load(file)
    else:
        customers_data = {}
    customers_data[order['phone']] = order['name']
    with open(file_path, 'w') as file:
        json.dump(customers_data, file, indent=4)
    print(f"Customer '{order['name']}' with phone number '{order['phone']}' added successfully.")

    file_path = "items.json"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            item_data = json.load(file)
    else:
        item_data = {}
    for item in order['items']:
        item_data[item['name']] = item['price']
    with open(file_path, 'w') as file:
        json.dump(item_data, file, indent=4)