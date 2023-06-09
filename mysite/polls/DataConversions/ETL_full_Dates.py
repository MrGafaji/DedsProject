from SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd

from ETL_AenC1 import ComposedateTable as ac1Dates
from ETL_AdventureWorks import ComposedateTable as adwDates

base = db()

def merge():
    print(1)
    ac1 = ac1Dates()
    print(3)
    adw = adwDates()
    # adw = adw.rename({'order_date':'OrderDate'})

    Dates = pd.concat([ac1, adw], ignore_index=True)    
    # _, row = next(Dates.iterrows())
    # print('first row:')
    # print(4)
    # print(type(row['order_date'].date()))
    # print(row.info())
    for _, row in Dates.iterrows():
        rowDict = row.to_dict()
        print(rowDict)
        newDict = {
            'order_date'    : str(rowDict['order_date'].date()),
            'year'          : rowDict['year'],
            'month'         : rowDict['month'],
        }

        base.InsertIntoTable('F_Order_dates', newDict)    


if __name__ == '__main__':
    merge()