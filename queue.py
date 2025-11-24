import collections
import threading

class OrderQueue:
    def __init__(self):
        self._orders = collections.deque()
        self._lock = threading.Lock()

    def add_order(self, order):
        """Přidá objednávku na konec fronty."""
        with self._lock:
            self._orders.append(order)

    def get_order(self):
        """Vrátí a odstraní objednávku ze začátku fronty."""
        with self._lock:
            if self._orders:
                return self._orders.popleft()
            return None

    def is_empty(self):
        """Zkontroluje, zda je fronta prázdná."""
        with self._lock:
            return not self._orders