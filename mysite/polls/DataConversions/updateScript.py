#from ETL_full_Dates import *
#from ETL_full_Klant import *
#from ETL_full_Leverancier import *
#from ETL_full_Product import *
#from ETL_full_State import *
import json
from django.http import HttpResponse


def Update_All_Final_Tables(response):
    response = "updated"
    return HttpResponse(response)




if __name__ == '__main__':
    Update_All_Final_Tables()