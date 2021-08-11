import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)
files
print (files)

files_xlsx = [f for f in files if f[-4:] == 'xlsx']
files_xlsx
print(files_xlsx)

df = pd.DataFrame()

for f in files_xlsx:
    data = pd.read_excel(f, 'All_suppliers')
    df = df.append(data)

df.to_excel("All_Suppliers_Merged.xlsx", index=False)

