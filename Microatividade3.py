import pandas as pd

df = pd.read_csv('dados.csv', sep=';', engine='python')

pd.set_option('display.max_rows', 9999)

print(df.to_string())
