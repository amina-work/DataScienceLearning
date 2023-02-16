import pandas as pd

df = pd.read_excel(
    io='/home/amina/Desktop/per/python-programs/dashboard_one/facilities.xlsx',
    engine="openpyxl",
    sheet_name="Tracking Covid-19 in Prisons Facilities",
    skiprows=3,
    #usecols="B:R",
    nrows=2640,
)

print(df)