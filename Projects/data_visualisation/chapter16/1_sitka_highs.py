# DOWNLOADING DATA

# Parsing the csv File Headers
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Printing the headers and ther positions
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2],"%Y-%m-%d")
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)
     
    
# print(highs)

# PLOTTING DATA IN A TEMPERATURE CHART

# Plot high and low temperatures.

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, color = "red")

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize = 24)
fig.autofmt_xdate()
ax.set_xlabel("", fontsize = 16)
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()

# PLOTTING DATES

