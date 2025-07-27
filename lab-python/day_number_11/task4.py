import pandas as pd
import numpy as np

data = pd.DataFrame()

for i in range(int(input())):
    s = input().split()
    data.loc[i, 'id'] = int(s[1])
    data.loc[i, 'neural'] = float(s[5])

d1 = data.groupby(by='id').min()
d2 = data.groupby(by='neural').max()
d = d1.merge(d2, left_on='id', right_on='id')
print(d)
d['delta'] = d['neural_y'] - d['neural_x']
a, b = np.unique(data['id'], return_counts=True)
d = d.drop(a[b == 1]).sort_values('delta')
anw = d.index.to_list()[0:3]
if len(anw) == 0:
    print(-1)
else:
    for i in anw:
        print(int(i), end=' ')
