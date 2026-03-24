import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#creamos dicionario con la base de datos
data = { 
    'genero': ['M', 'F', 'M', 'F'],
    'leer': [1, 0, 1, 1],
    'deporte': [0, 1, 1, 0],
    'viajar': [1, 0, 1, 1]
}
df = pd.DataFrame(data)
print("datos originales:")
print(df)
#creamos un df con la data

#aplicamos el melt
#---------------------
#convertimos la columna 'leer', 'deporte', 'viajar' en formato largo
#mantenemos a genero como 'genero como identificado'
df_melt = pd.melt(df,
                    id_vars=['genero'],
                    value_vars=['leer', 'deporte', 'viajar'])
print("\nDatos despues de melt:")
print(df_melt)

#agrupar y contar
#entonces agrupamos por genero, variable y su valor, para luego contar (ver cuantos hay)
df_counts = df.melt.groupby(['genero', 'variable', 'valor']).size().rst_index(name='total')
print("\ndatos despues del groupby y size")
print(df_counts)

#dibujamos el catplot
g=sns.catplot(x='variable', y='total', hue='valor', col='genero', data=df_counts, kind='bar', height=5, aspect=1 )
#guaradar la imagen par verla codespace
plt.savefig(grafico_practica.png)










