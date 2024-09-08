from random import randint
import pandas as pd
import numpy as np
from pprint import pprint

with open('pandas_.txt', 'w') as file:
    for _ in range(10_000_000):
        file.write(str(randint(-10_000_000, -1)) + ' ')
        file.write(str(randint(1, 10_000_000)) + ' ')

with open('pandas_.txt') as file:
    data = map(int, file.read().split())

a = {'positive': [], 'negative': []}

for integer in data:
    match integer > 0:
        case True:
            a['positive'].append(integer)
        case False:
            a['negative'].append(integer)

data = pd.DataFrame(a)
data = data.sort_values(by=['positive'], ascending=True, kind='heapsort')
data.index = [ind for ind in range(1, 10_000_001)]
pprint(data)
pprint(data.iloc[randint(1, 10_000_000)])
