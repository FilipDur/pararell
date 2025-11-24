import unittest
import os
from app import get_next_order_id, ORDERS_FILE

class TestApp(unittest.TestCase):

    def setUp(self):
        """Metoda, která se spustí před každým testem. Uklidí testovací soubor."""
        if os.path.exists(ORDERS_FILE):
            os.remove(ORDERS_FILE)

    def tearDown(self):
        """Metoda, která se spustí po každém testu. Uklidí testovací soubor."""
        if os.path.exists(ORDERS_FILE):
            os.remove(ORDERS_FILE)

    def test_get_next_order_id_no_file(self):
        """
        Testuje získání ID, když soubor s objednávkami neexistuje.
        Očekávaný výsledek je 1.
        """
        self.assertEqual(get_next_order_id(), 1)

    def test_get_next_order_id_empty_file(self):
        """
        Testuje získání ID, když je soubor prázdný (obsahuje pouze hlavičku).
        Očekávaný výsledek je 1.
        """
        with open(ORDERS_FILE, 'w') as f:
            f.write('order_id,product,quantity\n')
        
        self.assertEqual(get_next_order_id(), 1)

    def test_get_next_order_id_with_existing_orders(self):
        """
        Testuje získání ID, když soubor již obsahuje nějaké objednávky.
        Očekávaný výsledek je poslední ID + 1.
        """
        with open(ORDERS_FILE, 'w') as f:
            f.write('order_id,product,quantity\n')
            f.write('1,Kolo,1\n')
            f.write('2,Auto,5\n')
            f.write('3,Motorka,2\n')

        self.assertEqual(get_next_order_id(), 4)


if __name__ == '__main__':
    unittest.main()