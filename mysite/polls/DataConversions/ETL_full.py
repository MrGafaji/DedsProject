import ETL_AenC1
import ETL_AenC2
import ETL_AdventureWorks
import ETL_BideStore
import pandas as pd
from SupabaseInterface import SupabaseInterface as db, genID

def mergeProductDataFrames():
    idgen = genID()
    AC1 = ETL_AenC1.ComposeProductTable()
    AC2 = ETL_AenC2.ComposeProductTable()
    ADW = ETL_AdventureWorks.ComposeProductTable()
    for i in [AC1,AC2,ADW]:
        print(i.info())

    Columns = ['s_id', 'id', 'name', 'description']

    Product = pd.concat([AC1,AC2,ADW], ignore_index=True)
    iter= Product.iterrows()
    
    # for i in range(10):
    #     for j in range(10):
    #         next(iter)
    #     rowDict = next(iter)[1].to_dict()
    #     newDict = {
    #         'id': 3003, 
    #         's_id':idgen.id(), 
    #         'name': 'TestProd', 
    #         'description': '8 meter tall', 
    #         'sub_Category': 'Katten', 
    #         'category': 'Dieren'}
    #     print(row, type(row))
    # #     print(row['name'])


    # db.InsertIntoTable('F_Product', ent)
    return Product




if __name__ == '__main__':
    data = mergeProductDataFrames()

    # print(data)
    # print(data.info())
    # print(data.columns)