from supabase import create_client, Client
import pandas as pd
import json
from datetime import datetime
import copy

class genID():
    def __init__(self, prefix = None, start = 0) -> None:
        self.prefix = 's_'
        if prefix: 
            self.prefix = prefix
        self.number = start 
    
    def id(self):
        self.number += 1
        return self.prefix + str(format( self.number, '000005d'))

class SupabaseInterface:
    def __init__(self) -> None:
        pass

        self.url: str = 'https://cglhcfmkwabxrvlfuqwb.supabase.co/'
        self.key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNnbGhjZm1rd2FieHJ2bGZ1cXdiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODQxNDk2MzUsImV4cCI6MTk5OTcyNTYzNX0.h-qRysp76hKecbDCjdLaZP03wOaAQ_sl-6_vQ1odb7M"

        self.client: Client = create_client(self.url, self.key)
        # data = self.client.auth.sign_in_with_password({"email": "outdoorfusion@gmail.com", "password": "Admin123"})

    def GetFullTable(self, table, offset=0):
        '''loads a full table, concatinates multiple queries if necessary'''
        data = self.client.table(table).select('*').range(offset, offset+10000).execute().json()
        data = json.loads(data)
        data = data['data']
        data = pd.DataFrame.from_dict(data, orient='columns')
        if data.shape[0] == 1000:
            data = pd.concat([data, self.GetFullTable(table, offset=offset+1000)],ignore_index=True)
        return data

    def InsertIntoTable(self, table:str, entry:dict):
        self.client.table(table).insert(entry).execute()
 
    def GetFirstEntryWhere(self, table, where):
        try:
            query = self.client.table(table).select('*') 
            for key, value in where.items():
                query = query.eq(key, value)
            return query.execute().data[0]
        except IndexError:
            return None
        

    def AddIfNotAlreadyInDB(self, table, entry):
        
        exists = self.GetFirstEntryWhere(table, {
            'order_id':entry['order_id'], 
            'orderline_id': entry['orderline_id'], 
            'quantity':entry['quantity']
            })
        # print(f'{exists = }')
        if exists:
            print('Is Alredy in db')
            return
        try:
            self.client.table(table).insert(entry).execute()
            print('Inserted')
        except:
            pass
            
        




if __name__ == '__main__':
    idgen = genID()
    db = SupabaseInterface()
    # ent = {'id': 3003, 's_id':idgen.id(), 'name': 'TestProd', 'description': '8 meter tall', 'sub_Category': 'Katten', 'category': 'Dieren'}
    # db.InsertIntoTable('F_Product', ent)

    # data = db.GetFullTable('SalesOrderHeader')
    # print(type(data))
    # print(data)
    # print(data.info())
    # for i in range(10):
    #     print(idgen.id())

    res = db.GetFirstEntryWhere('F_Product', {"id":601})['s_id']

    print(res)
    print(type(res))
    # print(res)