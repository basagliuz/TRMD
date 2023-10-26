# Importo un paio di librerie utili

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import random as rnd

# Creo un dataframe con Pandas

data_dict = {'JD': [2458135.5, 2458135.5, 2458135.5, 2458140.5, 2458140.5, 2458140.5, 2458240.5, 2458240.5, 2458240.5],
   'object': ['A1689', 'A1689', 'A2218', 'A1689', 'A1689', 'A2218', 'A1689', 'A370', 'A2218'],
   'band': ['J', 'K', 'J', 'J', 'K', 'J', 'J', 'K', 'J']}
df1 = pd.DataFrame(data_dict)

# Creo una nuova colonna di numeri casuali e vedo se l'ho inserita bene

df1['random'] = np.random.rand(9)

print(df1)