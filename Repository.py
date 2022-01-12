import atexit
import sys
import sqlite3
from Suppliers import Suppliers
from Hats import Hats
from Orders import Orders

class Repository:

    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.suppliers = Suppliers(self._conn)
        self.hats = Hats(self._conn)
        self.orders = Orders(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
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
atexit.register(repo._close)
