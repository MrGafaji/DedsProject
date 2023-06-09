from DataConversions.SupabaseInterface import SupabaseInterface as db, genID

import pandas as pd



def ETL():

    ### Extract
    base = db()
    idgen = genID(prefix='c_')

    employee = base.GetFullTable('Employee')
    department = base.GetFullTable('Department')


    empDict = {'emp_id': employee['emp_id'],
             'dept_id': employee['dept_id'],
             'bene_health_ins' : employee['bene_health_ins'],
             'bene_day_care' : employee['bene_day_care'],
             'emp_fname' : employee['emp_fname'],
             'emp_lname' : employee['emp_lname'],
             'salary' : employee['salary'],
             }
    empFrame = pd.DataFrame(empDict)

    deptDict = {
        'dept_id' : department['dept_id'],
        'dept_name' : department['dept_name'],
    }
    deptFrame = pd.DataFrame(deptDict)

    fullframe = pd.merge(empFrame, deptFrame, on='dept_id', how='left')
    # print(fullframe)

    for _, row in fullframe.iterrows():
        rowDict = row.to_dict()
        newDict = {
            'emp_id'            : rowDict['emp_id'],
            'dept_id'           : rowDict['dept_id'],
            'dept_name'         : rowDict['dept_name'],
            'bene_health_ins'   : rowDict['bene_health_ins'],
            'bene_day_care'     : rowDict['bene_day_care'],
            'emp_fname'         : rowDict['emp_fname'],
            'emp_lname'         : rowDict['emp_lname'],
            'salary'            : rowDict['salary'],
        }

        base.AddIfNotAlreadyInDBForOtherTables('F_Employee', newDict, ['emp_id'])




if __name__ == '__main__':
    data = ETL()