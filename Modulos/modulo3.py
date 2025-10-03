import pandas as pd

datos = { 'Nombre': ['Luis', 'Julia', 'Yesenia', 'Mario', 'Daniel'],
         'Edad': [23, 35, 19, 32, 24],
         'Altura': [1.57, 1.69, 1.78, 1.90, 1.65],
         'Grado': ['Química', 'Diseño', 'Matemáticas', 'Ingenieria', 'Arquitectura'],
         'Correo': ['a@a.com', 'b@b.com', 'c@c.com', 'd@d.com', 'e@e.com'],
         'Vigente': [True, False, True, True, True]
}

df = pd.DataFrame(datos)

print(df)
print(df.loc[0])
print(df.loc[[1, 4]])
df = pd.DataFrame(datos, index = ["alumno1", "alumno2", "alumno3", "alumno4", "alumno5"])
print(df.loc["alumno4"])
