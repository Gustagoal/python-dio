import pandas as pd 

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#Somando os valores nulos
print(df.isnull().sum())  

# Removendo os valores ausentes 
df_clear = df.dropna()
print(df_clear.isnull().sum())  

# Substituindo os valores ausentes 

df["Age"] = df["Age"].fillna("Teste")
# print(df.isnull().sum())  
print(df["Age"])
