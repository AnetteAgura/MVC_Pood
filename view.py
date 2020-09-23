import pandas as pd

class View:
    # show items
    def showItems(self, items):
        print("============================")
        print("Shop items")
        print("============================")
        df = pd.DataFrame(columns=['Name', 'Price', 'Amount'])
        for item in items:
            df = df.append({'Name': item.getName(), 'Price': item.getPrice(), 'Amount': item.getAmount()}, ignore_index=True)
        print(df)

    # show item
    def showItem(self, item):
        print("============================")
        print("Shop item {}.".format(item.getName()))
        print("============================")
        df = pd.DataFrame(columns=['Name', 'Price', 'Amount'])
        df = df.append({'Name': item.getName(), 'Price': item.getPrice(), 'Amount': item.getAmount()},
                        ignore_index=True)
        print(df)

    def noItemError(self, name):
        print("Shop do no not consist item {}.".format(name))
        print("============================")