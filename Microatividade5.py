import pandas as pd

df = pd.read_csv('dados.csv', sep=';', engine='python')

print("--- INFORMAÇÕES GERAIS ---")
df.info()