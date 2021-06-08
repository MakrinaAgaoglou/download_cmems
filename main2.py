import argparse
import json

from src.download_cmems import global_data #if we want to import more data from download_cmems we do it like that : ,ibi_data

parser = argparse.ArgumentParser()
parser.add_argument("--json", help="insert your json file", required = True)
args = parser.parse_args()

with open(args.json) as f:
    jdata = json.load(f)

print(jdata)
#exit()

#my_first_dict = {
#        "date0": "2021-06-07",
#        "number_of_days":1,
#        "lonmin": 2,
#        "lonmax": 3,
#        "latmin": 1,
#        "latmax": 2
#        }

global_data(jdata)
#global_data("2021-04-01")
#global_data("2021-06-07", 2)
