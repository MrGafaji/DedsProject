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
    # for i in [AC1,AC2,ADW]:
    #     print(i.info())

    # Columns = ['s_id', 'id', 'name', 'description']

    Product = pd.concat([AC1,AC2,ADW], ignore_index=True)
    # iter= Product.iterrows()
    
    for _, row in Product.iterrows():
        # for j in range(10):
        #     next(iter)
        rowDict = row.to_dict()
        newDict = {
            'id': rowDict['id'], 
            's_id':idgen.id(), 
            'name': rowDict['name'],
            'description': rowDict['description'],
        }
        if type(newDict['description']) == float or not newDict['description']:
            # if newDict['name']
            newDict['description'] = "not provided" 
        
        print(newDict['description'], type(newDict['description'])) 
            # newDict['description'] = 'None'
           
        print(newDict, type(newDict))

        base.InsertIntoTable('F_Product', newDict)
    return Product




if __name__ == '__main__':
    data = mergeProductDataFrames()

    # print(data)
    # print(data.info())
    # print(data.columns)