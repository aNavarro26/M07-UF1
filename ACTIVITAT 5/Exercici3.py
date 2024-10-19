import pandas as pd 
import matplotlib.pyplot as plt

arxiu = pd.read_csv("ACTIVITAT 5\\mobiles.csv")

#prepapamos los ids en una lista

ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]


def mostrarClockSpeed ():
    #en aquesta linea filtrem en la primera part las filas que els valors de id que tenen existeix en la lista que hem creat, despres selecciona nomes las dues columnas que volem
    clockSpeed_data = arxiu[arxiu["id"].isin(ids)][["id", "clock_speed"]]

    print(clockSpeed_data)


def mostrarMegaPixels():
    
    migaPixel_data = arxiu[arxiu["id"].isin(ids)][["id", "px_height"]]
    print(migaPixel_data)


def mostrarbatteryPower():
    
    battery_data = arxiu[arxiu["id"].isin(ids)][["id", "battery_power"]]
    print(battery_data)

"""he estata fent proves en aquesta part, al prinicipi ho tenía repetitiu, es a dir, que amb cada funció feía aixó:
fig, ax = plt.subplots()
ax.bar(clockSpeed_data["id"], clockSpeed_data["clock_speed"], color='blue')
ax.set_title('Clock Speed by Mobile ID')
ax.set_xlabel('Mobile ID')
ax.set_ylabel('Clock Speed (GHz)')
 plt.show()
 Pero al final he descubert que es pot fer una funció per totes, ja que les tres fan lo mateix.
"""
def plot_data(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 5))
    plt.bar(data['id'], data[ylabel], color='blue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def main():
    
    mostrarClockSpeed()
    mostrarMegaPixels()
    mostrarbatteryPower()


     # Cargar datos para graficar
    clockSpeed_data = arxiu[arxiu["id"].isin(ids)][["id", "clock_speed"]]
    migaPixel_data = arxiu[arxiu["id"].isin(ids)][["id", "px_height"]]
    battery_data = arxiu[arxiu["id"].isin(ids)][["id", "battery_power"]]

    # Graficar datos
    plot_data(clockSpeed_data, 'Clock Speed by Mobile ID', 'Mobile ID', 'clock_speed')
    plot_data(migaPixel_data, 'Megapixels by Mobile ID', 'Mobile ID', 'px_height')
    plot_data(battery_data, 'Battery Power by Mobile ID', 'Mobile ID', 'battery_power')



main()


