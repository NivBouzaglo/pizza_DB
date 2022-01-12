# DAO Object
from DTO import Hat


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
                       INSERT INTO hats (id, topping, supplier, quantity ) VALUES (?, ?, ?, ?)
                   """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def set_quantity(self, hat):
        self._conn.execute("""
                    UPDATE hats
                    SET quantity = quantity-1  
                    WHERE id=?
        """, [hat.id])

    def remove(self, hat):
        self._conn.execute("""
                    DELETE FROM hats
                    WHERE id= ?
        """, [hat.id])

    def find(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT * FROM hats WHERE id = ?
                """, [hat_id])
        return Hat(*c.fetchone())


    def find_by_topping(self, hat_topping):
        c = self._conn.cursor()
        c.execute("""
                            SELECT * FROM hats WHERE topping = ? ORDER BY supplier
                        """, [hat_topping])
        return Hat(*c.fetchone())

