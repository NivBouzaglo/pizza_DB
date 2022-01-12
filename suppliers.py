from DTO import Supplier


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                       INSERT INTO suppliers (id, name) VALUES (?, ?)
                   """, [supplier.id, supplier.name])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT * FROM suppliers WHERE id = ?
                """, [supplier_id])
        return Supplier(*c.fetchone())