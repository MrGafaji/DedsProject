from SupabaseInterface import SupabaseInterface as db, genID
import pandas as pd

from ETL_AenC1 import ComposedateTable as ac1Dates
from ETL_AdventureWorks import ComposedateTable as adwDates


def merge():
    print(1)
    ac1 = ac1Dates()
    print(3)
    adw = adwDates()

    for i in [ac1, adw]:
        print(i.info())


if __name__ == '__main__':
    merge()