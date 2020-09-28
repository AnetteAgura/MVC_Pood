# ui.py

# import classes and files
from product import Product
from shop import Shop
from controller import Controller
from model import Model
from view import View
from stock import Stock
from model_stock import stockM

# create products
bread = Product("bread", 0.80, 25)
milk = Product("milk", 0.50, 50)
wine = Product("wine", 5.60, 20)

# create shop and add products to shop
shop = Controller(Model(Shop()), View())
stock = Controller(stockM(Stock()), View())
stock.addItem("bread", 0.80, 25)
stock.addItem("milk", 0.50, 50)
stock.addItem("wine", 5.60, 20)

shop.restock("milk", 0.50, 10)
shop.showItems()

stock.showItems()
