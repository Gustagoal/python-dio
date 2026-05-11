import pandas as pd 

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

table = pd.read_csv(url)

print(table.info())