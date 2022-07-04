"""
Módulo de graficación de precios diarios.
-------------------------------------------------------------------------------
Se crea un gráfico de líneas que representa los precios promedios diarios, usando el archivo data_lake/business/precios-diarios.csv y la salida se salva en formato PNG en
data_lake/business/reports/figures/daily_prices.png.
"""


def make_daily_prices_plot():

    import pandas as pd
    import matplotlib.pyplot as plt

    path_file = r"data_lake/business/precios-diarios.csv"
    datos = pd.read_csv(path_file, index_col=None, sep=",", header=0)
    datos["fecha"] = pd.to_datetime(datos["fecha"])
    x = datos.fecha
    y = datos.precio

    plt.figure(figsize=(15, 6))
    plt.plot(x, y, "b", label="Promedio Diario")
    plt.title("Promedio Diario")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.legend()
    plt.xticks(rotation="vertical")
    plt.savefig("data_lake/business/reports/figures/daily_prices.png")


if __name__ == "__main__":

    try:

        import doctest

        doctest.testmod()

        make_daily_prices_plot()

    except:
        raise NotImplementedError("Implementar esta Función")
