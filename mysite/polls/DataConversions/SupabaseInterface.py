from supabase import create_client, Client
import pandas as pd
import json
from datetime import datetime

class genID():
    def __init__(self, prefix = None) -> None:
        self.prefix = 's_'
        if prefix: 
            self.prefix = prefix
        self.number = 0 
    
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
        




if __name__ == '__main__':
    idgen = genID()
    db = SupabaseInterface()
    # ent = {'id': 3003, 's_id':idgen.id(), 'name': 'TestProd', 'description': '8 meter tall', 'sub_Category': 'Katten', 'category': 'Dieren'}
    # db.InsertIntoTable('F_Product', ent)

    data = db.GetFullTable('SalesOrderHeader')
    print(type(data))
    print(data)
    print(data.info())
    # for i in range(10):
    #     print(idgen.id())