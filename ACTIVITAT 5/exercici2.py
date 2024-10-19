import pandas as pd
import matplotlib.pyplot as plt


def Poblacio_total():
    #Guardamos el contenido del csv en archivo utilizando las columnos City y Population
    archivo = pd.read_csv('List_of_world_cities_by_population_density.csv', usecols=['City', 'Population'])
    #Eliminamos el ultimo numero que esta entre '[]'
    archivo['Population'] = archivo['Population'].replace({r'[^\d.]': ''}, regex=True).astype(float)
    #Nos devuelve las 10 primeras lineas
    return archivo.head(10)


def DensitatKm2_City():
    archivo = pd.read_csv('List_of_world_cities_by_population_density.csv', usecols=['City', 'Density (/km²)'])
    return archivo.head(10)


def DensitatMi2_City():
    archivo = pd.read_csv('List_of_world_cities_by_population_density.csv', usecols=['City', 'Density (/mi²)'])
    return archivo.head(10)

def main():
    # Guardamos los datos de las funciones en estas variables
    poblacion = Poblacio_total()
    densidad_km2 = DensitatKm2_City()
    densidad_mi2 = DensitatMi2_City()

    
    plt.figure(figsize=(15, 7)) #Definir las medidas de la ventana
    plt.subplot(2, 2, 1)  # Subplot 1
    #Definimos que el grafico sea circular y como queremos que sea el contenido
    plt.pie(poblacion['Population'], labels=poblacion['City'], autopct='%1.1f%%', startangle=140) 
    plt.title("Población Total") #Indicamos el titulo del grafico
    plt.legend(poblacion['City'], bbox_to_anchor=(1, 0.5), loc="center left") #Definimos la leyenda y hacemos que no este encima del grafica

    plt.subplot(2, 2, 2)  # Subplot 2
    plt.pie(densidad_km2['Density (/km²)'], labels=densidad_km2['City'], autopct='%1.1f%%', startangle=140)
    plt.title("Densidad (/km²)")
    plt.legend(densidad_km2['City'], bbox_to_anchor=(1, 0.5), loc="center left")

    plt.subplot(2, 2, 3)  # Subplot 3
    plt.pie(densidad_mi2['Density (/mi²)'], labels=densidad_mi2['City'], autopct='%1.1f%%', startangle=140)
    plt.title("Densidad (/mi²)")
    plt.legend(densidad_mi2['City'], bbox_to_anchor=(1, 0.5), loc="center left")

    # Mostrar gráficos
    plt.tight_layout()
    plt.show()
    
main()

