from DataConversions.SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd

def ETL():
    ### Extract
    base = db()
    idgen = genID(prefix='s_')

    vendorTable = base.GetFullTable('Vendor')
    frame = {'id': vendorTable['BusinessEntityID'],
             'name': vendorTable['Name'],
             }
    vendors = pd.DataFrame(frame)

    for _, row in vendors.iterrows():
        rowDict = row.to_dict()
        newDict = {
            's_id'      : idgen.id(),
            'id'        : rowDict['id'],
            'name'      : rowDict['name'],
        }

        base.AddIfNotAlreadyInDBForOtherTables('F_Vendor', newDict, ['id', 'name'])
        # print(newDict)



if __name__ == '__main__':
    data = ETL()