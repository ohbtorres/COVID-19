# Leitura de arquivos CSV com auxilio do pyarrow
from pyarrow import csv, Table

def pa_read_csv(source,sep=","):
    return csv.read_csv(source,parse_options=csv.ParseOptions(delimiter=sep)).to_pandas()

def pa_write_csv(datafram_pandas,file_name):
	csv.write_csv(data = Table.from_pandas(datafram_pandas),output_file = file_name)