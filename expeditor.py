import threading
import time

class OrderExpeditor(threading.Thread):
    def __init__(self, processed_queue):
        super().__init__()
        self.processed_queue = processed_queue
        self.running = True

    def run(self):
        while True:
            order = self.processed_queue.get_order()
            if order:
                print(f"Odesílám {order}")
                time.sleep(1)  # simulace expedice
            else:
                if not self.running and self.processed_queue.is_empty():
                    break # Ukončí smyčku, pokud je vlákno zastaveno a fronta prázdná
                time.sleep(0.1)

    def stop(self):
        self.running = False
