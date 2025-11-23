import pandas as pd

df = pd.read_excel('excel-ai/dio-excel.xlsx')

print(df["Game Name"].unique())