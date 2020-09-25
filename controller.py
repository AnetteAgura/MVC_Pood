import exceptions

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Ok!")
        except:
            print("Problem!")

    def showItems(self):
        try:
            items = self.model.showItems()
            self.view.showItems(items)
        except:
            print("No items to show.")

    def showItem(self, name):
        try:
            item = self.model.showItem(name)
            self.view.showItem(item)
        except:
            self.view.noItemError(name)

    def deleteItem(self, name):
        try:
            self.model.deleteItem(name)
            self.view.deleteItem(name)
        except:
            print("Failed to delete item.")

    def deleteAll(self):
        try:
            self.model.deleteAll()
            self.view.deleteAll()
        except:
            print("There are no items to show.")

# elemendi uuendamine
    def updateItem(self, name, price, amount):
        if (price <= 0):
            print("Price must be higher then 0 EUR")
        elif (amount <= 0):
            print("Amount must be higher than 0")
        try:
            self.model.updateItem(name, price, amount)
            self.view.updateItem()
        except:
            self.view.noItemError(name)