#numpy & pandas work only 3.10.6 python version
#also I uninstalled jupyter so it won't work
import pandas as pd
import numpy as np

SHEET_ID = '1oMrHuOkbXAoXibN6UzHUkNrwqvjQVFOU8CuqFMVZiUo'
SHEET_NAME = '2010174370'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid={SHEET_NAME}'

df = pd.read_csv(url, on_bad_lines='skip')
print(df.head())