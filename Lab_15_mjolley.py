'''
Data Visualization
Michael Jolley
This code reads a CVS file and compiles a graph based on the data
'''

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


filename = 'OHRU.csv'

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

  
    print("Header information:")
    for index, column_header in enumerate(header_row):
        print(f"{index}: {column_header}")


    dates, rates = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            unemployment_rate = float(row[1])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            rates.append(unemployment_rate)


plt.figure(figsize=(14, 6))
plt.plot(dates, rates, color='blue', linewidth=1)


plt.title("U.S. Unemployment Rate Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)

plt.gca().xaxis.set_major_locator(mdates.YearLocator(5))  # every 5 years
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gcf().autofmt_xdate()  # rotate date labels

plt.grid(True)
plt.tight_layout()
plt.show()
