from SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd




def ETL():

    ### Extract
    base = db()
    idgen = genID(prefix='c_')

    sales = base.GetFullTable('Sales')
    frame = {'age': sales['Customer_Age'],
             'age_group': sales['Age_Group'],
             'gender' : sales['Customer_Gender']
             }
    customers = pd.DataFrame(frame)
    customers = customers[['age', 'age_group', 'gender']].value_counts().reset_index(name='count')

    for _, row in customers.iterrows():
        rowDict = row.to_dict()
        newDict = {
            'id'            : idgen.id(),
            'age'           : rowDict['age'],
            'age_group'     : rowDict['age_group'],
            'gender'        : rowDict['gender'],
            'count'         : rowDict['count']
        }

        base.AddIfNotAlreadyInDBForOtherTables('F_Klant', newDict, ['age', 'gender'])



if __name__ == '__main__':
    data = ETL()