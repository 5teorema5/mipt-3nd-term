import pandas as pd

data = pd.read_csv('doc/transactions.csv')
sorted_data = data.loc[data['STATUS'] == 'OK'].sort_values('SUM', ascending=False).reset_index()

print('TASK_1')
for i in range(3):
    print(f'{sorted_data.loc[i, 'SUM']} \t -> {sorted_data.loc[i, 'CONTRACTOR']}')

print('TASK_2')
data_Umbrella = data.loc[data['CONTRACTOR'] == 'Umbrella, Inc']
data_Umbrella = data_Umbrella.loc[data_Umbrella['STATUS'] == 'OK']
print(f'Σ = {data_Umbrella.sum().loc['SUM']} \t -> Umbrella, Inc')
