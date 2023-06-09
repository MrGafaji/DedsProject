from DataConversions.SupabaseInterface import SupabaseInterface as db, genID

import pandas as pd
def AddFirstCountries():
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

        base.AddIfNotAlreadyInDBForOtherTables('F_State', rowDict, ['state'])

def ETL():

    ### Extract
    base = db()
    idgen = genID(prefix='s_')
    AddFirstCountries()

    sales = base.GetFullTable('Sales')
    frame = {'state': sales['State'],
             'country': sales['Country'],
             }
    customers = pd.DataFrame(frame)
    customers = customers[['state', 'country']].value_counts().reset_index(name='count')

    for _, row in customers.iterrows():
        rowDict = row.to_dict()
        newDict = {
            's_id'      : idgen.id(),
            'state'     : rowDict['state'],
            'country'   : rowDict['country'],
            'count'     : rowDict['count'],
        }

        base.AddIfNotAlreadyInDBForOtherTables('F_State', newDict, ['state'])



if __name__ == '__main__':
    data = ETL()