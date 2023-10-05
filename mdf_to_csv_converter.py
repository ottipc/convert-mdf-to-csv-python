from mdfreader import Mdf
import pandas as pd

def mdf_to_csv(input_mdf_file, output_csv_file):
    # MDF-Datei öffnen
    mdf_file = Mdf(input_mdf_file)

    # Daten aus der MDF-Datei extrahieren
    data = mdf_file.export_to_pandas()

    # Daten in CSV exportieren
    data.to_csv(output_csv_file, index=False)

# Beispielaufruf der Funktion
input_mdf_file = '/home/codi/Entwicklung/EI St. Augustin/oh.mdf'
output_csv_file = '/home/codi/Entwicklung/mdf-to-csv-python/CSV/oh.csv'
mdf_to_csv(input_mdf_file, output_csv_file)

