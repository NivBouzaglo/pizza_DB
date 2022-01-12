import sys
from Repository import repo
import Hats
from DTO import Hat
from DTO import Order
from DTO import Supplier

if __name__ == "__main__":
    main(args)

def main(args):
    sys.argv
    repo.create_table()
    config_text = open(sys.argv[0], "r+").read()
    numbers_hats = 0
    numbers_suppliers = 0
    counter = 0
    for line in config_text.split('\n'):
        split = line.split(',')
        if counter == 0:
            numbers_suppliers = split[0]
            numbers_hats = split[1]
        elif 0 < counter <= numbers_hats:
            hat = Hat(split[0], split[1], split[2], split[3])
            repo.hats.insert(hat)
        else:
            supplier = Supplier(split[0], split[1])
            repo.suppliers.insert(supplier)
        counter += 1

    orders = open(sys.argv[1], "r+").read()
    orderID = 1
    output = ""
    for order in orders.split('\n'):
        split = order.split(',')
        location = order[0]
        topping = order[1]
        pizza = repo.hats.find_by_topping(topping)
        if pizza is not None:
            repo.hats.set_quantity(pizza)
            if pizza.quantity == 0:
                repo.hats.remove(pizza)
        else:
            print("This topping is over")
        ord = Order(orderID, location, pizza.id)
        repo.orders.insert(ord)
        orderID += 1

        s = repo.suppliers.find(pizza.supplier)
        output += topping + ',' + s.name + ',' + location + '\n'

    txt = open(sys.argv[2], "w")
    txt.write(output)
    txt.close()
