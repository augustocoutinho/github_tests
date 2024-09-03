import pandas as pd

path = './input/data_1.csv'

df = pd.read_csv(path)
df.to_csv('./output/output.csv', index=False)

print(df)