# Primo esercizio della lezione del 26 ottobre 2023.

# Dato un dataframe, creare una nuova colonna con entrate casuali. Usare numpy.

# =============================================================================

# Importo le librerie necessarie.

import pandas as pd
import numpy as np

# Il dataframe dato è...

data_dict = {'JD': [2458135.5, 2458135.5, 2458135.5, 2458140.5, 2458140.5, 2458140.5, 2458240.5, 2458240.5, 2458240.5],
             'object': ['A1689', 'A1689', 'A2218', 'A1689', 'A1689', 'A2218', 'A1689', 'A370', 'A2218'],
             'band': ['J', 'K', 'J', 'J', 'K', 'J', 'J', 'K', 'J']}
df = pd.DataFrame(data_dict)
print(df)

# Creo una n-upla di numeri casuali con numpy. Scelgo numeri casuali tra 0 e 1.

nc = np.random.rand(9)
print(nc)

# Inserisco "random numbers" (rn) nel mio dataframe.

df['random numbers'] = nc
print(df)

# Esercizio completato.