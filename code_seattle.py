#.2
import json
with open("precipitation.json","r", encoding="utf-8") as file:
	precipitation_data=json.load(file)	

Seattle_measurements = []               # list of dictionaries of measurements made at Seattle (emtpy for now)

for measurement in precipitation_data:
    if measurement["station"]== "GHCND:US1WAKG0038":
        Seattle_measurements.append(measurement)           # adds the dictionaries of Seattle measurements to the list

# calculating precipitation per month 

precipitation_per_month_Seattle = []
for i in range(12):
    precipitation_per_month_Seattle.append(0)   # creates a list with 12 elements set to 0, each element of the list corresponding to total percipitation in a given month

for measurement in Seattle_measurements:
    date = str(measurement["date"])     # access the date of the measurement and tell the program that is is a string variable
    month = date.split("-")[1]        # splits the date sting at the "-", creating a list, and selects the 2nd element of the list -> the month
    index = int(month) - 1                     # the month the measurement was made in corresponds to the index on the list of monthly total percipitation
    precipitation_per_month_Seattle[index] += measurement["value"]      # calculates the total percipitation per month in the precipitation_per_month_Seattle list

# 2.1 calculating total yearly precipitation per site

total_yearly_precipitation_Seattle = 0
for month in precipitation_per_month_Seattle:
    total_yearly_precipitation_Seattle += month

# 2.2 relative monthly precipitation
relavive_monthly_precipitation = []

for month in precipitation_per_month_Seattle:
    relavive_monthly_precipitation.append(month/total_yearly_precipitation_Seattle)


# formating the final results.json file:
results = {}
Seattle_resuls = {}
results["Seattle"] = Seattle_resuls
Seattle_resuls["station"] = "GHCND:US1WAKG0038"
Seattle_resuls["state"] = "WA"
Seattle_resuls["total_monthly_precipitation"] = precipitation_per_month_Seattle
Seattle_resuls["total_yearly_precipitation"] = total_yearly_precipitation_Seattle 
Seattle_resuls["relative_monthly_precipitation"] = relavive_monthly_precipitation


with open("results.json","w") as file:
	json.dump(results,file, indent=4)           # saves the results as a json file


 
