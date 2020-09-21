import pandas as pd
class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        df = pd.DataFrame(items)
        print(df)