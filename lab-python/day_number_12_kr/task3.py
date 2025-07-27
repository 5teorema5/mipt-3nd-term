import pandas as pd
import numpy as np

data = pd.DataFrame()

for i in range(int(input())):
    s = input().split(';')
    o = s[1].strip()
    data.loc[i, 'num'] = s[0].strip()
    if o[-1] in ['D', 'Д']:
        data.loc[i, 'od'] = 'OD'
        data.loc[i, 'os'] = ''
    else:
        data.loc[i, 'os'] = 'OS'
        data.loc[i, 'od'] = ''

data = data.groupby(by='num').sum()
a = np.array(data['od'].to_list())
b = np.array(data['os'].to_list())
c = len(a)
od = len(a[a != ''])
os = len(b[b != ''])
print(c, od+os, od, os, sep='\n')
