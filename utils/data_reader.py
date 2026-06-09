import csv, json

def read_user_csv():
    with open("data/users.csv", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def read_products_json():
    with open ("data/products.json") as file:
        return json.load(file)