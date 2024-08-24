import pandas as pd

Numeros = range(50,70,2)

print(type(Numeros))

Numeros_serie = pd.Series(Numeros)
print(Numeros_serie)