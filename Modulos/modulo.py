import pandas as pd

s = pd.Series(["Historia", "Matemáticas", "Español", "Biología", "Química"], dtype="string")

print(s)

print("El tamaño de la series:", s.size)
print("Sus indices son:", s.index)