import pandas as pd

class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        df = pd.DataFrame(columns=['Name', 'Price', 'Amount'])
        for item in items:
            df = df.append({'Name': item.getName(), 'Price': item.getPrice(), 'Amount': item.getAmount()}, ignore_index=True)
        print(df)