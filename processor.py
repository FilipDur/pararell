import threading
import time

class OrderProcessor(threading.Thread):
    def __init__(self, order_queue, processed_queue):
        super().__init__()
        self.order_queue = order_queue
        self.processed_queue = processed_queue
        self.running = True

    def run(self):
        while True:
            order = self.order_queue.get_order()
            if order:
                print(f"Zpracovávám {order}")
                time.sleep(1)  
                self.processed_queue.add_order(order)
            else:
                if not self.running and self.order_queue.is_empty():
                    break # Ukončí smyčku, pokud je vlákno zastaveno a fronta prázdná
                time.sleep(0.1)

    def stop(self):
        self.running = False
