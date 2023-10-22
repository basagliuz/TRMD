# Esercizio 2 della lezione del 20 ottobre 2023 di TRMD.
# Utilizzare i dati contenuti in es2.dat per creare un grafico.
# Le colonne utili sono "M_ass", 'b-y', 'age_parent[Gyr]'.
# L'esercizio è diviso in due parti:
#  I. creare uno scatter in cui tutti i punti abbiano colori diversi;
#  II. creare uno scatter con varie classi di colori.

# ===================================================

# Importo i pacchetti e le librerie necessarie.

import numpy as np
import matplotlib.pyplot as mpl

# Importo i dati in tre array.

file = 'es2.dat'
data = np.loadtxt(file, delimiter = ' ', usecols = (4, 8, 12), unpack = True)
m = data[0]
b = data[1]
a = data[2]

# Posso passare al punto I.

# =========================

# I. creo uno scatter in cui tutti i punti abbiano colori diversi.
# Plotto il mio grafico tramite scatter usando colori diversi.

mpl.scatter(b, m, c = a, cmap = 'winter_r', marker = '.', s = 5)
k = mpl.scatter(b, m, c = a, cmap = 'winter_r', marker = '.', s = 5)

# Imposto l'intervallo di visualizzazione e dò un nome agli assi.

mpl.xlim(-0.1, 1)
mpl.ylim(8.5, -4)

mpl.xlabel('b-y')
mpl.ylabel('M_V')

# Aggiungo una colorbar con il comando colorbar e aggiungo un label.
# La scala dei colori è data da 'age_parent'.

mpl.colorbar(k, label = 'Gyr')

# Salvo la figura ottenuta in questo modo. Pulisco il canvas.

mpl.savefig('es2I.png')
mpl.clf()

# Posso passare al punto II.

# ========================== 


# II. Creo uno scatter con varie classi di colori
# Devo usare l'array 'data' per associare a ciascuna coppia (m, b) il colore giusto.
# Cerco minimo e massimo del vettore 'age_parent' (data[2]).

mn = min(data[2])
mx = max(data[2])

# Seleziono il numero di classi e creo due vettori contenti gli estremi inf/sup.

nc = 15
d = (mx - mn)/nc
inf = []
sup = []
for i in range(nc):
  inf = inf + [i*d]
  sup = sup + [(i + 1)*d]

# Plotto un grafico per ciascuna classe. 
# Arrotondo il numero di cifre per gli array da usare come legenda.

inf_l = np.around(inf, decimals = 1)
sup_l = np.around(sup, decimals = 1)

for i in range(nc):
  id_i = np.where(data[2] <= sup[i])
  id_s = np.where(data[2][id_i] >= inf[i])
  mpl.scatter(data[1, id_s], data[0, id_s], marker = '.', s = 5, label = ("{} Gyr - {} Gyr" .format(inf_l[i], sup_l[i])))

# Imposto l'intervallo di visualizzazione e dò un nome agli assi. Creo una legenda.

mpl.xlim(-0.1, 1)
mpl.ylim(8.5, -4)

mpl.xlabel('b-y', size = 'small')
mpl.ylabel('$M_V$', size = 'small')

mpl.legend(fontsize = 'x-small')

# Salvo la figura ottenuta in questo modo.

mpl.savefig('es2II.png')

# Esercizio completato.