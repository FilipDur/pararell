import data_processor

def main():
    """
    Hlavní funkce programu.
    """
    csv_file_path = 'orders.csv'
    
    print("Zpracovávám soubor s objednávkami...")
    summary = data_processor.summarize_products_from_file(csv_file_path)
    
    if summary:
        print("\n--- Souhrn produktů ---")
        for product, total_quantity in summary.items():
            print(f"Produkt: {product:<15} | Celkem kusů: {total_quantity}")

if __name__ == "__main__":
    main()