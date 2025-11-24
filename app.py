import csv
import os
from order import Order
from queue import OrderQueue
from processor import OrderProcessor
from expeditor import OrderExpeditor
 
ORDERS_FILE = 'orders.csv'
 
def get_next_order_id():
    """Získá další ID objednávky na základě existujících záznamů v souboru."""
    if not os.path.exists(ORDERS_FILE) or os.path.getsize(ORDERS_FILE) == 0:
        return 1
    with open(ORDERS_FILE, 'r', newline='') as f:
        # Přečte poslední řádek souboru pro získání posledního ID
        try:
            last_line = f.readlines()[-1]
            if last_line.strip():
                last_id = int(last_line.split(',')[0])
                return last_id + 1
        except (IndexError, ValueError):
            # Soubor je prázdný nebo obsahuje jen hlavičku
            return 1
    return 1
 
def main():
    # Vytvoření front pro komunikaci mezi vlákny
    order_queue = OrderQueue()
    processed_queue = OrderQueue()
 
    # Vytvoření a spuštění vláken pro zpracování a expedici
    processor = OrderProcessor(order_queue, processed_queue)
    expeditor = OrderExpeditor(processed_queue)
 
    processor.start()
    expeditor.start()
 
    print("Systém pro zpracování objednávek je aktivní.")
    print("Zadejte 'konec' pro ukončení aplikace.")
 
    try:
        while True:
            product = input("Produkt: ")
            if product.lower() == 'konec':
                break
            try:
                quantity_input = input("Množství: ").strip()
                quantity = int(quantity_input)
                order_id = get_next_order_id()
                order = Order(order_id, product, quantity)
 
                with open(ORDERS_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([order.order_id, order.product, order.quantity])
 
                order_queue.add_order(order)
                print(f"Objednávka č. {order_id} přijata ke zpracování.")
 
            except ValueError:
                print("Chyba: Množství musí být celé číslo.")
 
    except KeyboardInterrupt:
        print("\nUkončování aplikace...")
 
    processor.stop()
    expeditor.stop()
    processor.join()
    expeditor.join()
    print("Aplikace byla bezpečně ukončena.")
 
if __name__ == "__main__":
    main()
