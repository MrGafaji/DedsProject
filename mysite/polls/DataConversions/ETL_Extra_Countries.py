
from SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd



def addToDB():
    idgen = genID(prefix='s_')
    base = db()
    countries  = [(1, 'Northwest', 'US', 'North America'),
    (2, 'Northeast', 'US', 'North America'),
    (3, 'Central', 'US', 'North America'),
    (4, 'Southwest', 'US', 'North America'),
    (5, 'Southeast', 'US', 'North America'),
    (6, 'Canada', 'CA', 'North America'),
    (7, 'France', 'FR', 'Europe'),
    (8, 'Germany', 'DE', 'Europe'),
    (9, 'Australia', 'AU', 'Pacific'),
    (10, "United Kingdom", 'GB', 'Europe')]
    colnames = ('TerritoryID', 'Name', 'CountryRegionCode', 'Group') 

    for c in countries:
        rowDict = {
            's_id': c[0],
            'state': c[1],
            'country': c[3]
        }

        base.InsertIntoTable('F_State', rowDict)
    
        

if __name__ == '__main__':
    addToDB()

