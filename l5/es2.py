# Secondo esercizio della lezione del 26 ottobre 2023.

# Prima di procedere con la consegna, importo le librerie necessarie.

import pandas as pd
import numpy as np

# ===================================================================

# Considero un dataframe importato da un file csv.

planets = pd.read_csv('planets.csv')

# Posso mostrare la media di un certa colonna (e.g. periodi orbitali) in questo modo. 
# Ho scelto arbitrariamente di mostrare i dati raggruppandoli per metodo. 

medie_1 = planets.groupby('method')['orbital_period'].mean()
print(medie_1)

# Ripetere lo stesso processo usando numpy.

# =========================================

# Creo una funzione che estragga il valore medio della colonna di un dataframe.

def my_mean(df, col = 'orbital_period'):
  return np.mean(df[col])

# Applico la funzione tramite il comando apply.

medie_2 = planets.dropna(subset = 'orbital_period').groupby('method').apply(my_mean)
print(medie_2)

# Esercizio terminato.