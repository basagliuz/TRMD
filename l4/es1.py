# Primo esercizio della lezione di TRMD del 20 ottobre 2023.
# Creare due array (ad esempio con numpy.arange()).
# Inserire almeno 10 zeri nel secondo array.
# L'obiettivo è quello di computare il prodotto tra il primo e il secondo array.
# Bisogna farlo in tre modi:
#  I. identificando gli zeri del secondo array e computando solo le entrate non nulle;
#  II. sostituendo gli zeri del secondo array con 0.001 e computando il tutto;
#  III. ignorando gli zeri del secondo array e computando il tutto.
# Nel caso III. vanno identificati gli inf con numpy.isinf().

# Importo numpy.

import numpy as np

# Creo i due array.

a = np.arange(0, 10, 0.5)
b = np.arange(0, 16, 0.8)
na, = a.shape
nb, = b.shape
print("Primo array: \n {} \n Dimensione: \n {}" .format(a, na))
print("Secondo array: \n {} \n Dimensione: \n {}"  .format(b, nb))

# Inserisco gli zeri nel secondo array.

bz = b
for i in range(0, 20, 2):
  bz[i] = 0
print("Secondo array con zeri: \n {}" .format(bz))

# I: identifico gli zeri del secondo array. Computo solo le entrate non nulle.

z, = np.where(bz != 0)
c1 = a[z]/bz[z] 
nc1, = c1.shape
print("Quoziente del primo tipo: \n {} \n Dimensione \n {}" .format(c1, nc1))

# II: sostituisco gli zeri del secondo array. Computo tutto.

bqz = np.where(b == 0, 0.001 , bz)
nbqz, = bqz.shape
print("Secondo array con (quasi) zeri: \n {} \n Dimensione: \n {}" .format(bqz, nbqz))
c2 = a/bqz
nc2, = c2.shape
print("Quoziente del secondo tipo: \n {} \n Dimensione \n {}" .format(c2, nc2))

# III: eseguo la divisione tra gli array originali e cerco gli infiniti.

c3 = a/b
nc3, = c3.shape
print("Quoziente del terzo tipo: \n {} \n Dimensione: \n {}" .format(c3, nc3))
inf = np.isinf(c3)
ninf = []
for i in range(nc3):
  if inf[i]:
    ninf = ninf + [i]
  else:
    continue
print("Posizione degli infiniti nel quoziente: \n {}" .format(ninf))

# Esercizio completato!