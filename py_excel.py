import pandas as pd
import openpyxl

df = pd.read_excel('data.xlsx', index_col='Ответственный')

df.loc['UserName_1'].to_excel("UserName_1.xlsx")
df.loc['UserName_2'].to_excel("UserName_2.xlsx")
df.loc['UserName_3'].to_excel("UserName_3.xlsx")

