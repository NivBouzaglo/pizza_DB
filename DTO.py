# DTO Objects
class Hat:
    def _init_(self, id, topping, supplier, quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Order:
    def _init_(self, id, location, hat):
        self.id = id
        self.location = location
        self.hat = hat


class Supplier:
    def _init_(self, id, name):
        self.id = id
        self.name = name
