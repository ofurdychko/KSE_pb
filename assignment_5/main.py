import requests
# Kyiv:
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 50.4547,
	"longitude": 30.5238,
	"hourly": ["temperature_2m", "wind_speed_10m"]
}
response = requests.get(url, params=params)
data = response.json()
# print(data)

import pandas as pd
data_by_hours = data['hourly']
df = pd.DataFrame(data_by_hours)
# print(df)

temp_dataframe = df.iloc[0:72,1]
#print(temp_dataframe)
max_temp = temp_dataframe.max()
min_temp = temp_dataframe.min()
mean_temp = temp_dataframe.mean()
# print(max_temp)

wind_dataframe = df.iloc[:,2]
# print(wind_dataframe)
overall_mean_windspeed = wind_dataframe.mean()
#print(overall_mean_windspeed)
hours_counter = 0 
for i in wind_dataframe:
    if i > overall_mean_windspeed:
        hours_counter += 1 
# print(hours_counter)

# There is also an advanced method from the last lecture:
# hours_counter = sum(1 for i in wind_dataframe if i > overall_mean_windspeed)
# print(hours_counter)