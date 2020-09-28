import helpers_stock

class stockM:
    # get shop data - [] of products
    def __init__(self, itemsStock):
        self.itemsStock = itemsStock
    # add item to items
    def addItem(self, name, price, amount):
        helpers_stock.addItem(name, price, amount)
    # show items
    def showItems(self):
        return helpers_stock.showItems()
    # show item
    def showItem(self, name):
        return helpers_stock.showItem(name)
    # delete item
    def deleteItem(self, name):
        helpers_stock.deleteItem(name)
    # delete all items
    def deleteAll(self):
        helpers_stock.deleteAll()
    # elemendi uuendamine
    def updateItem(self, name, price, amount):
        helpers_stock.updateItem(name, price, amount)