import sys
from Repository import repo
import Hats
from DTO import Hat
from DTO import Order
from DTO import Supplier


repo.create_tables()
config_text = open(sys.argv[1], "r+").read()
numbers_hats = 0
list = []
numbers_suppliers = 0
counter = 0
for line in config_text.split('\n'):
    split = line.split(',')
    if counter == 0:
        numbers_suppliers = split[1]
        numbers_hats = split[0]
    elif counter < int(numbers_hats) or counter == int(numbers_hats):
        hat = Hat(split[0], split[1], split[2], split[3])
        repo.hats.insert(hat)
    else:
        supplier = Supplier(split[0], split[1])
        repo.suppliers.insert(supplier)
    counter += 1

orders = open(sys.argv[2], "r+").read()
orderID = 1
output = ""
for order in orders.split('\n'):
    orderSplit = order.split(',')
    location = orderSplit[0]
    topping = orderSplit[1]
    pizza = repo.hats.find_by_topping(topping)
    if pizza is not None:
        repo.hats.set_quantity(pizza)
        if pizza.quantity-1 == 0:
            repo.hats.remove(pizza)
    else:
        print("This topping is over")
    ord = Order(orderID, location, pizza.id)
    repo.orders.insert(ord)
    orderID += 1

    s = repo.suppliers.find(pizza.supplier)
    output += topping + ',' + s.name + ',' + location + '\n'

txt = open(sys.argv[3], "w")
txt.write(output)
txt.close()
