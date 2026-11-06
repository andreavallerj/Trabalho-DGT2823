import pandas as pd

df = pd.read_csv('dados.csv', sep=';', engine='python')

print("\n--- Informações gerais  ---")
df.info()

print("\n--- Primeiras linhas ---")
print(df.head(3))

print("\n--- Últimas linhas  ---")
print(df.tail(3))


df_tratado = df.copy()


df_tratado['Calories'] = df_tratado['Calories'].fillna(0)

df_tratado['Date'] = df_tratado['Date'].fillna('1900/01/01')
df_tratado['Date'] = df_tratado['Date'].replace('1900/01/01', pd.NA)
df_tratado['Date'] = df_tratado['Date'].replace('20201226', '\'2020/12/26\'')
df_tratado['Date'] = df_tratado['Date'].replace('\'', "")


df_tratado['Date'] = pd.to_datetime(df_tratado['Date'], format="'%Y/%m/%d'")

df_tratado = df_tratado.dropna()

print("\n--- Copia com os valores corrigidos ---")
print(df_tratado)