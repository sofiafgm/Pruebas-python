import pandas as pd

s = pd.Series([70, 25, 40, 55, 70, 80, 95, 55, 60, 105])

print("Contiene:", s.count(), "elementos")
print("La suma de la serie es:", s.sum())
print("La suma acumulada es:", s.cumsum())
print(s.value_counts())
print("El valor mínimo es:", s.min())
print("El valor máximo es:", s.max())
print("La media es:", s.mean())
print("La desviación estándar es:", s.std())
print(s.describe())