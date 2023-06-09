from DataConversions.SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd

from DataConversions.ETL_AenC1 import ComposedateTable as ac1Dates
from DataConversions.ETL_AdventureWorks import ComposedateTable as adwDates

base = db()

def ETL():
    ac1 = ac1Dates()
    adw = adwDates()

    Dates = pd.concat([ac1, adw], ignore_index=True)    
    # print(row.info())
    for _, row in Dates.iterrows():
        rowDict = row.to_dict()
        print(rowDict)
        newDict = {
            'order_date'    : str(rowDict['order_date'].date()),
            'year'          : rowDict['year'],
            'month'         : rowDict['month'],
        }

        base.AddIfNotAlreadyInDBForOtherTables('F_Order_dates', newDict, ['order_date'])    


if __name__ == '__main__':
    ETL()