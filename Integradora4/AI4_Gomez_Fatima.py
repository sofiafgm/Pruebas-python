import pandas as pd

df = pd.read_csv('/Users/jaimeglez/Sofia/Python/Integradora4/Morbilidad.csv', encoding='utf-8')

print(df.to_string()) 

'''


stats = df.agg(
    {
        "casos": ["min", "max", "median", "mean", "sum"],
        "tasa": ["min", "max", "median", "mean", "sum"],
    }
)

print(stats)


def sumar_casos_por_causa(ruta_csv):

    df['causas'] = df['causas'].str.replace(r'[\n\r\t\u200b]', '', regex=True)
    
    resumen = ruta_csv.groupby('causas', as_index=False)['casos'].sum()
    
    resumen.rename(columns={'casos': 'casos_totales'}, inplace=True)
    
    return resumen

resultado = sumar_casos_por_causa(df)

print(resultado.head())

'''