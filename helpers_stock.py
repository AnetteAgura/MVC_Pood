import exceptions
from product import Product

# repsresents shop structure
# list of Product type objects
itemsInStock = []

# add item to items
def addItem(name, price, amount):
    global itemsInStock
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in itemsInStock:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        itemsInStock.append(product)

# show items
def showItems():
    global itemsInStock
    # control if items exists
    if len(itemsInStock) == 0:
        raise exceptions.ItemExists("List of items is empty.")
    else:
        return itemsInStock

# show item
def showItem(name):
    global itemsInStock
    # control all items step by step
    for item in itemsInStock:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemExists("Not found {} item.".format(name))
# delete ONE item
def deleteItem(name):
    global itemsInStock
    for item in itemsInStock:
        # if the name is the same as we search
        if (item.getName() == name):
            itemsInStock.remove(item)
        else:
            continue
            raise exceptions.ItemExists("Not found {} item.".format(name))
# delete all
def deleteAll():
    global itemsInStock
    itemsInStock.clear()

# update item
def updateItem(name, price, amount):
    global itemsInStock
    for item in itemsInStock:
        if (item.getName() == name):
            price = item.setPrice(price)
            amount = item.setAmount(amount)
        else:
            raise exceptions.ItemNotExists("Item {} can't be updated, because it does not exist.".format(name))

def moveItem(name, price, amount):
    global itemsInStock
    for item in itemsInStock:
        if(item.getName() == name):
            aamount = item.getAmount()
            item.amount = item.setAmount(aamount-amount)
        else:
            continue
            raise exceptions.ItemExists("Item {} can't be moved.".format(name))