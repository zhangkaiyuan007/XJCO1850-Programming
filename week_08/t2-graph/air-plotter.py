'''
You have been provided with ‘leeds-central-air-quality.csv’ which is a file containing air quality data for Leeds from the last few years. There are 4 values – particulate matter (25), particulate matter (10), Ozone and Nitrous Oxide which are all different measures of air quality – which are recorded against the date.
Load this file into a suitable data structure.

From this data, create a line plot of the average of the 4 data points against the date.

For example, for the row:
07/09/2024,68,20,25,5

You would plot a point at (68+20+25+5)/4 = 29.5

The X-axis should be the date, the Y-axis should be the average pollution.
'''
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def main():
    dates = []
    averages = []
    
    with open('leeds-centre-air-quality.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            if not row or len(row) < 5 or not row[0].strip():
                continue
            
            try:
                date = row[0].strip()
                pm25 = float(row[1])
                pm10 = float(row[2])
                o3 = float(row[3])
                no2 = float(row[4])
                
                avg_val = (pm25 + pm10 + o3 + no2) / 4
                dates.append(date)
                averages.append(avg_val)
            except ValueError:
                continue

    dates.reverse()
    averages.reverse()

    plt.figure(figsize=(12, 6))
    ax = plt.gca()
    
    plt.plot(dates, averages, color='teal', linewidth=2, marker='o', markersize=4)
    
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))
    
    plt.title('Average Air Quality in Leeds Over Time')
    plt.xlabel('Date')
    plt.ylabel('Average Pollution Level')
    
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
