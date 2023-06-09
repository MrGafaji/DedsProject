import ETL_full_Dates 
import ETL_full_Klant 
import ETL_full_Leverancier 
import ETL_full_Product 
import ETL_full_State 
import ETL_full_Medewerker
import ETL_full_Order_Feittabel

import json
from django.http import HttpResponse


def Update_All_Final_Tables(response):
    ETL_full_Dates.ETL()
    ETL_full_Klant.ETL()
    ETL_full_Leverancier.ETL()
    ETL_full_Product.ETL()
    ETL_full_State.ETL()
    ETL_full_Medewerker.ETL()
    ETL_full_Order_Feittabel.ETL_Fact()
    response = "updated"
    return HttpResponse(response)




if __name__ == '__main__':
    Update_All_Final_Tables('r')