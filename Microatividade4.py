import pandas as pd

df = pd.read_csv('dados.csv', sep=';', engine='python')

print("--- PRIMEIRAS 10 LINHAS ---")
print(df.head(10))

print("\n--- ÚLTIMAS 10 LINHAS ---")
print(df.tail(10))