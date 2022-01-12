import sys
from Repository import repo
from DTO import Hat,Order,Supplier

repo.create_table()
config_text = open("config.txt" , "r").read()
numbers_of_hats = int(config_text[0:config_text.find(,)])
number_of_supplier = int(config_text[',']+1:config_text.find('\n'))
counter = 0
for line in config_text.split('\n')
    split = line.split(',')
    if counter <= numbers_of_hats:
        hat =Hat(split[0] , split[1], split[2] , split[3])
        repo.hats.insert(hat)


