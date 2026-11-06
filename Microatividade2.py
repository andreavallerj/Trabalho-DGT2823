import pandas as pd

df = pd.read_csv('dados.csv', sep=';', engine='python')

df_subconjunto = df[['Duration', 'Pulse', 'Calories']]

print(df_subconjunto)
