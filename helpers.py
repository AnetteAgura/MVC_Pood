import exceptions
from product import Product

# repsresents shop structure
# list of Product type objects
items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemExists("List of items is empty.")
    else:
        return items
# show item
def showItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item.".format(name))
# delete ONE item
def deleteItem(name):
    global items
    for item in items:
        # if the name is the same as we search
        if (item.getName() == name):
            items.remove(item)
        else:
            continue
            raise exceptions.ItemExists("Not found {} item.".format(name))
# delete all
def deleteAll():
    global items
    items.clear()

# update item
def updateItem(name, price, amount):
    global items
    for item in items:
        if (item.getName() == name):
            item.price = item.setPrice(price)
            item.amount = item.setAmount(amount)
        else:
            continue
            raise exceptions.ItemNotExists("Item {} can't be updated, because it does not exist.".format(name))
