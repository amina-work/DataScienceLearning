import pandas as pd



df = pd.read_excel(
    io='/home/amina/Desktop/per/python-programs/dashboard_one/facilities.xlsx',
    engine="openpyxl",
    sheet_name="Tracking Covid-19 in Prisons Facilities",
    skiprows=3,
    #usecols="B:R",
    nrows=2640,
)

with open('/home/amina/Desktop/per/python-programs/dashboard_one/facilities.xlsx', 'wb') as outFile:
    outFile.write(df)
    outFile.close()   # was missing this
    with zipfile.ZipFile('/home/amina/Desktop/per/python-programs/dashboard_one/facilities.xlsx', 'r') as zip:
        zip.extractall(destination)
print(df)