# DAO Object
from DTO import Order


class Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
                       INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
                   """, [order.id, order.location, order.hat])

    def find(self, order_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT * FROM orders WHERE id = ?
                """, [order_id])
        return Order(*c.fetchone())
