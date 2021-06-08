import os
import subprocess
import datetime

from dotenv import load_dotenv

load_dotenv()

#date0="2021-05-01"
#datef="2021-05-01"

#print("today_is:", datetime.datetime.now()) # this prints the date of today

#t0 = datetime.datetime.strptime(date0, "%Y-%m-%d") #we decided to delete this part %H:%M:%S.%f")

#get_my_date = t0.strftime("%Y-%m-%d %H:%M:%S")

#time_step = datetime.timedelta(days=1) # this adds one day. We can also add hours (hours=1) or minutes or seconds 
#print(time_step)
#print(t0)
#print(get_my_date)
#print(t0 + time_step)

#exit()
def global_data(data):

    for i in range(data["number_of_days"]):
        t0 = datetime.datetime.strptime(data["date0"], "%Y-%d-%m")
        cmd = f"""
            python -m motuclient \
            --motu https://nrt.cmems-du.eu/motu-web/Motu \
            --service-id GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS \
            --product-id global-analysis-forecast-phy-001-024 \
            --longitude-min {data["lonmin"]} \
            --longitude-max {data["lonmax"]} \
            --latitude-min {data["latmin"]} \
            --latitude-max {data["latmax"]} \
            --date-min {data["date0"]} \
            --date-max {data["date0"]} \
            --depth-min 0.493 \
            --depth-max 0.4942 \
            --variable uo \
            --variable vo \
            --out-dir ./ \
            --out-name global_{data["date0"]}.nc \
            --user {os.environ.get("username")} --pwd {os.environ.get("passwd")}
        """
        p = subprocess.Popen(cmd, shell=True)
        p.wait()
        #t0 += time_step
        t0 += datetime.timedelta(days=1)
        date0 = t0.strftime("%Y-%m-%d")

    my_output = "!!!DONE!!!"
    return my_output




