import csv
from collections import defaultdict

def summarize_products_from_file(file_path):
    product_quantities = defaultdict(int)

    try:
        with open(file_path, mode='r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 3:
                    product_name = row[1].strip()
                    quantity = int(row[2].strip())
                    product_quantities[product_name] += quantity
    except FileNotFoundError:
        print(f"Chyba: Soubor '{file_path}' nebyl nalezen.")
        return None

    return dict(product_quantities)