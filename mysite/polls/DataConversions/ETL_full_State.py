from SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd




def ETL():

    ### Extract
    base = db()
    idgen = genID(prefix='s_')

    sales = base.GetFullTable('Sales')
    frame = {'state': sales['State'],
             'country': sales['Country'],
             }
    customers = pd.DataFrame(frame)
    customers = customers[['state', 'country']].value_counts().reset_index(name='count')

    for _, row in customers.iterrows():
        rowDict = row.to_dict()
        newDict = {
            's_id'        : idgen.id(),
            'state'     : rowDict['state'],
            'country'   : rowDict['country'],
        }

        base.InsertIntoTable('F_State', newDict)
        print(newDict)



if __name__ == '__main__':
    data = ETL()