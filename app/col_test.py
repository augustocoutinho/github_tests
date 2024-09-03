import pandas as pd
import re

path = './output/output.csv'
df = pd.read_csv('./output/output.csv')


def test_cols(df):
    col_names = df.columns

    result = [bool(re.match(r'^qtd|^dat|^cod', i)) for i in col_names]

    if all(result) == True:
        return 'Todas as coluna atendem ao padrão estabelecido!'
    else:
        return 'Revise as colunas, elas aparentam ter o nome fora da nomenclatura!'


print(test_cols(df = df))
print('deu certo!')
