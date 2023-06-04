import ETL_AenC1
import ETL_AenC2
import ETL_AdventureWorks
import ETL_BideStore
import pandas as pd

def mergeProductDataFrames():
    AC1 = ETL_AenC1.ComposeProductTable()
    AC2 = ETL_AenC2.ComposeProductTable()
    ADW = ETL_AdventureWorks.ComposeProductTable()

    pd.DataFrame()
    for df in [AC1, AC2, ADW]:
        print(f'{df.columns}')




if __name__ == '__main__':
    mergeProductDataFrames()