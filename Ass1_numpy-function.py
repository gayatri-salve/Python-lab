#1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

#Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
import numpy as np

import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

hot_days = np.where(temperatures > 35)[0] + 1
hot_temperatures = temperatures[temperatures > 35]

cold_days = np.where(temperatures < 5)[0] + 1
cold_temperatures = temperatures[temperatures < 5]

print("Hot Days:")
print("Day\tTemperature (°C)")
for day, temp in zip(hot_days, hot_temperatures):
    print(f"{day}\t{temp}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
for day, temp in zip(cold_days, cold_temperatures):
    print(f"{day}\t{temp}")


#OUTPUT
Hot Days:
Day	Temperature (°C)
3	36.8
6	38.7
10	37.2

Cold Days:
Day	Temperature (°C)
8	4.0
9	-4.0
10	-12.0
