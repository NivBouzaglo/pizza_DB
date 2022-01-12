import atexit
import sqlite3
import Suppliers
import Hats
import Orders


class Repository:

    def _init_(self):
        self._conn = sqlite3.connect('DataBase.db')
        self.suppliers = _Suppliers(self._conn)
        self.hats = _Hats(self._conn)
        self.orders = _Orders(self._conn)

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
atexit.register(repo.close)
