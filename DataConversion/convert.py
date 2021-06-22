import argparse

from nptdms import TdmsFile
import pandas as pd
import os

'''
Script utilizzato per convertire il file di dati TDMS in formato CSV.
Analizzando i file dei sensori ricevuti, si nota che tutti i dati sono contenuti in un unico gruppo
definito Untitled e in un unico canale anch'esso definito Untitled. Sembra che inoltre i dati siano formati solamente
dai valori numerici. Non è presente alcuna indicazione sul timestamp.
'''

GROUP_NAME   = "Untitled"
CHANNEL_NAME = "Untitled"
TDMS_EXT     = ".tdms"

parser = argparse.ArgumentParser(description="Converts a TDMS file to CSV.")
parser.add_argument("--source", required=True, help="TDML source file")
parser.add_argument("--out", help="Output file name (default: same name of source)")

args = parser.parse_args()

source_path = args.source.lower()
out_path = args.out
if(out_path == None):
    filename = os.path.basename(source_path)
    (file, ext) = os.path.splitext(filename)
    out_path = os.path.join(os.path.dirname(source_path), file + ".csv")

# Check source extension
if(source_path.endswith(TDMS_EXT) == False):
    exit("Error. Source file is not a TDMS file: " + source_path)

tdms_file = TdmsFile.read(source_path)
group = tdms_file[GROUP_NAME]
channel = group[CHANNEL_NAME]

dataframe = pd.DataFrame({ "Value": channel[:] })
#print(dataframe)

dataframe.to_csv(out_path, index=False)
