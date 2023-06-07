from SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd
import ETL_AenC1
import ETL_AenC2
import ETL_AdventureWorks as ETL_AW
import ETL_BideStore as ETL_BS

def ETL():
    base = db()
    idgen = genID(prefix='s_')

    AenC1 = ETL_AenC1.ComposeSalesOrder()
    AenC2 = ETL_AenC2.ComposeSalesOrder()
    AW = ETL_AW.ComposeSoldProductProductTable()
    BS = ETL_BS

    