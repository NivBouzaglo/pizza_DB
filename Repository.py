import atexit
import sqlite3
import suppliers
import hats

# The Repository
class Repository:

    def __init__(self):
        self._conn = sqlite3.connect('config.db')
        self.suppliers = _suppliers(self._conn)
        self.hats = _hats(self._conn)
        self.orders = _orders(self.connOrders);

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.execute("""
        CREATE TABLE hats (
            id      INTEGER         PRIMARY KEY,
            topping  STRING       NOT NULL,
            supplier INTEGER REFERENCES Supplier(id),
            quantity INTEGER NOT NULL
        );

        CREATE TABLE suppliers (
            id       INTEGER     PRIMARY KEY,
            name     STRING    NOT NULL
        );

        CREATE TABLE orders (
            id        INTEGER     PRIMARY KEY,
            location  STRING     NOT NULL,
            hat     INTEGER REFERENCES hats(id)
        );
       """)

repo = Repository()
atexit.register(repo.close)
