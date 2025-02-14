#.3
import json
with open("precipitation.json","r", encoding="utf-8") as file:
	precipitation_data=json.load(file)	

from csv import DictReader

with open("stations.csv","r", encoding = "utf-8") as file:
	stations=DictReader(file)
	stations_list = list(stations)      # list of dictionaries with keys "Location", "State" and "Station"

results = {}                          # defines the final results dictionary that will be imported to json

#calculating the total precipitation in all stations
total_rain = 0
for measurement in precipitation_data:
    total_rain += measurement["value"]

for station in stations_list:
    station_id = station["Station"]
    location_measurements = []               # list of dictionaries of measurements made at one location (emtpy for now)
    for measurement in precipitation_data:
        if measurement["station"] == station_id:
            location_measurements.append(measurement)           # adds the dictionaries of measurements at one location to the list

# calculating precipitation per month 

    precipitation_per_month = []
    for i in range(12):
        precipitation_per_month.append(0)   # creates a list with 12 elements set to 0, each element of the list corresponding to total percipitation in a given month

    for measurement in location_measurements:
        date = str(measurement["date"])     # access the date of the measurement and tell the program that is is a string variable
        month = date.split("-")[1]        # splits the date sting at the "-", creating a list, and selects the 2nd element of the list -> the month
        index = int(month) - 1                     # the month the measurement was made in corresponds to the index on the list of monthly total percipitation
        precipitation_per_month[index] += measurement["value"]      # calculates the total percipitation per month in the precipitation_per_month_Seattle list

# 2.1 calculating total yearly precipitation per site

    total_yearly_precipitation = 0
    for month in precipitation_per_month:
        total_yearly_precipitation += month

# 2.2 relative monthly precipitation
    relavive_monthly_precipitation = []

    for month in precipitation_per_month:
        relavive_monthly_precipitation.append(month/total_yearly_precipitation)


# formating the final results.json file:
    location_resuls = {}
    results[station["Location"]] = location_resuls
    location_resuls["station"] = station["Station"]
    location_resuls["state"] = station["State"]
    location_resuls["total_monthly_precipitation"] = precipitation_per_month
    location_resuls["total_yearly_precipitation"] = total_yearly_precipitation
    location_resuls["relative_monthly_precipitation"] = relavive_monthly_precipitation
    location_resuls["relative_yearly_precipitation"] = total_yearly_precipitation / total_rain


with open("results.json","w") as file:
    json.dump(results,file, indent=4)           # saves the results as a json file


 
