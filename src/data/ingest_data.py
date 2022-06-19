"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
"""


pip install wget

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.
    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.
    """
    
    
    import wget
    import os

    os.chdir("data_lake/landind/")
    for año in range (1995,2021):
        if año in range(2016,2018):
         wdir=("https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true".format(año))
         wget.download(wdir)
        else: 
         wget.download("https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xlsx/{}.xls?raw=true".format(año))
         wget.download(wdir)
        
    return
    
ingest_data()
#raise NotImplementedError("Implementar esta función")
    
if __name__ == "__main__":
    import doctest

    doctest.testmod()
