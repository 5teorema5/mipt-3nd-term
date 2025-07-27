import pandas as pd

games = pd.read_csv(input(), sep=';')
rates = pd.read_csv(input(), sep=';')

mean_marks = rates.groupby('id', as_index=False).mean()
data = pd.merge(games, mean_marks, on='id')

sorted_data = data.sort_values('mark', ascending=False)
sorted_data = sorted_data.reset_index()
for i in range(3):
    print(f'{sorted_data.loc[i, 'name']} {sorted_data.loc[i, 'mark']:.3f}')

data8 = data.loc[data['mark'] > 8.0]
a = data8.loc[:, "company"].value_counts().sort_values(ascending=False)
print(f'{a.index[0]} {a.iloc[0]}')
