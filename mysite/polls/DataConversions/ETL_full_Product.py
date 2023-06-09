import ETL_AenC1
import ETL_AenC2
import ETL_AdventureWorks
import ETL_BideStore
import pandas as pd
from SupabaseInterface import SupabaseInterface as db, genID

def mergeProductDataFrames():
    base = db()
    idgen = genID()
    AC1 = ETL_AenC1.ComposeProductTable()
    AC2 = ETL_AenC2.ComposeProductTable()
    ADW = ETL_AdventureWorks.ComposeProductTable()

    Product = pd.concat([AC1,AC2,ADW], ignore_index=True)    
    for _, row in Product.iterrows():
        rowDict = row.to_dict()
        newDict = {
            'id': rowDict['id'], 
            's_id':idgen.id(), 
            'name': rowDict['name'],
            'description': rowDict['description'],
        }
        if type(newDict['description']) == float or not newDict['description']:
            if ' - ' in newDict['name']:
                print('old', newDict)
                tup = newDict['name'].split(' - ')
                print(tup, type(tup))
                newDict['name'], newDict['description'] = tup[0], tup[1]
                print('new', newDict)
            else:
                newDict['description'] = "not provided" 
        

        base.InsertIntoTable('F_Product', newDict)
    return Product

# TODO: Better splitting of names into names and descriptions
# TODO: Make this script update the database if an entry is not in it

if __name__ == '__main__':
    data = mergeProductDataFrames()

    # print(data)
    # print(data.info())
    # print(data.columns)