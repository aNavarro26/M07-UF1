import pandas as pd
import matplotlib.pyplot as plt

# TODO: 1 funció que mostri per pantalla, la quantitat de casos total per mes per país (agafar 10 països) (agafar 4 mesos).


def casos_totals_per_mes_i_pais():

    dataframe = pd.read_csv("df_covid19_countries.csv")

    dataframe["date"] = pd.to_datetime(dataframe["date"])

    # converteixo a format date la data per desrés poder tractar els months i el year
    dataframe["month"] = dataframe["date"].dt.month
    dataframe["year"] = dataframe["date"].dt.year

    random_countries = dataframe["location"].drop_duplicates().sample(10)

    dataframe = dataframe[dataframe["location"].isin(random_countries)]

    ultim_any_per_pais = dataframe.groupby("location")["year"].max().reset_index()

    # combino dataframe amb el df ultim_any_per_pais amb "location" i "year"
    # posant inner indico que es quedaran les files que coincideixen amb "location" i "year", si no coincideixen s'eliminen
    dataframe = dataframe.merge(
        ultim_any_per_pais, on=["location", "year"], how="inner"
    )

    # gener, febrer, març, abril
    desired_months = [1, 2, 3, 4]
    dataframe_filtrado = dataframe[dataframe["month"].isin(desired_months)]

    # ordeno per date ascendent
    dataframe_filtrado = dataframe_filtrado.sort_values("date")
    total_casos_per_pais = (
        dataframe_filtrado.groupby(["location", "year", "month"]).last().reset_index()
    )

    # agafo les columnes que m'interessen
    total_casos_per_pais = total_casos_per_pais[
        ["location", "year", "month", "total_cases"]
    ]

    # print(total_casos_per_pais)
    return total_casos_per_pais


# TODO: 1 funció que mostri per pantalla, les morts totals per mes per país (agafar 10 països) (agafar 4 mesos) del 2021.


def morts_totals_per_mes_i_pais():
    dataframe = pd.read_csv("./df_covid19_countries.csv")

    # agafo els countries pero sense repetits
    all_countries = dataframe["location"].unique()

    # agafo 10 countries
    countries = pd.Series(all_countries).sample(10)

    dataframe["date"] = pd.to_datetime(dataframe["date"])

    dataframe["month"] = dataframe["date"].dt.month

    months = [5, 6, 7, 8]

    dataframe_filtrado = dataframe[
        dataframe["location"].isin(countries)
        & dataframe["month"].isin(months)
        & (dataframe["date"].dt.year == 2021)
    ]

    morts_filtrades = (
        dataframe_filtrado.groupby(["location", "month"])["total_deaths"]
        .sum()
        .reset_index()
    )

    # print(morts_filtrades)
    return morts_filtrades


# TODO: 1 funció que mostri per pantalla la “reproduction_rate” per mes per país (agafar 10 països) (agafar 4 mesos).


def reproduction_rate_per_mes_i_pais():
    dataframe = pd.read_csv("./df_covid19_countries.csv")

    all_countries = dataframe["location"].unique()
    countries = pd.Series(all_countries).sample(10)

    dataframe["date"] = pd.to_datetime(dataframe["date"])

    dataframe["month"] = dataframe["date"].dt.month

    months = [3, 4, 5, 6]

    dataframe_filtrado = dataframe[
        dataframe["location"].isin(countries) & dataframe["month"].isin(months)
    ]

    reproduction_rate_filtrado = (
        dataframe_filtrado.groupby(["location", "month"])["reproduction_rate"]
        .sum()
        .reset_index()
    )

    # print(reproduction_rate_filtrado)
    return reproduction_rate_filtrado


reproduction_rate_per_mes_i_pais()

# TODO: 1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica de línies per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda)


def main():
    # guardo els resultats de les funcions
    total_casos_per_pais = casos_totals_per_mes_i_pais()
    morts_filtrades = morts_totals_per_mes_i_pais()
    reproduction_rate_filtrado = reproduction_rate_per_mes_i_pais()

    # grafica principal
    grafica1 = plt.figure(num="Gráfica 1", figsize=(10, 10))

    ax1 = grafica1.add_subplot(3, 1, 1)  # grafica 1 (Casos Totales)
    ax2 = grafica1.add_subplot(3, 1, 2)  # grafica 2 (Muertes Totales)
    ax3 = grafica1.add_subplot(3, 1, 3)  # grafica 3 (Tasa de Reproduccin)

    # per a que no sorti amb notació científica
    ax1.ticklabel_format(style="plain")
    ax2.ticklabel_format(style="plain")
    ax3.ticklabel_format(style="plain")
    # casos totals per mes i país
    for pais in total_casos_per_pais["location"].unique():
        dades_pais = total_casos_per_pais[total_casos_per_pais["location"] == pais]
        ax1.plot(dades_pais["month"], dades_pais["total_cases"], label=pais)
    ax1.set_title("Total de casos per mes i país")  # Titol de la gráfica
    ax1.set_xlabel("Mes")  # Etiqueta eix X
    ax1.set_ylabel("Total de casos")  # Etiqueta eix Y
    ax1.legend(loc="upper left", bbox_to_anchor=(1, 1))  # la anclo a la dreta
    ax1.tick_params(axis="x", rotation=45)

    # morts totals per mes i país
    for pais in morts_filtrades["location"].unique():
        dades_pais = morts_filtrades[morts_filtrades["location"] == pais]
        ax2.plot(dades_pais["month"], dades_pais["total_deaths"], label=pais)
    ax2.set_title("Total de morts per mes i país (2021)")
    ax2.set_xlabel("Mes")
    ax2.set_ylabel("Total de morts")
    ax2.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax2.tick_params(axis="x", rotation=45)

    # reproduction_rate per mes i país
    for pais in reproduction_rate_filtrado["location"].unique():
        dades_pais = reproduction_rate_filtrado[
            reproduction_rate_filtrado["location"] == pais
        ]
        ax3.plot(dades_pais["month"], dades_pais["reproduction_rate"], label=pais)
    ax3.set_title("Reproduction rate per mes i país")
    ax3.set_xlabel("Mes")
    ax3.set_ylabel("Reproduction rate")
    ax3.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax3.tick_params(axis="x", rotation=45)

    plt.tight_layout()  # s'ajusta per a que no hi hagi objectes junts
    plt.show()


main()
