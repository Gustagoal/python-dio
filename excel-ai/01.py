import pandas as pd


df = pd.read_excel(r"C:\Users\Gustavo Castro\Desktop\python-dio\excel-ai\dio-excel.xlsx")

print(df["Region"].unique())