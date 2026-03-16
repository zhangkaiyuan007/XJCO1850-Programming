# Define a WeatherStation class to represent a weather station that collects
# temperature, humidity, and related weather data. This class will allow for recording
# new data (temperature, humidity), displaying the current weather data, and calculating
# average conditions over time.

# The WeatherStations class should have the following fields:
# (1) location: the location of the weather station (e.g., Leeds)
# (2) temperature: the current temperature in Celsius
# (3) humidity: the current humidity reading as a percentage (0 to 100)
# (4) data_log: a list of dictionary in which each dictionary contains recorded temperature
#     and humidity readings. For example [{"temperature": 22.5, "humidity": 45.0}, {"temperature": 20.0, "humidity": 55.0}]
# When an instance of WeatherStation is created, only the value of location is needed. The other fields are by default None or empty list.

# The class should have the following methods:
# (1) record_data(temp, hum) that records a new data entry for temperature and humidity. It updates the temperature and humidity
#     fields to the new values. It also adds a dictionary with temperature and humidity values to the data_log list.
# (2) display_current_conditions() that prints the current weather conditions including the location, temperature, and humidity.
#     For example
#     Current conditions at Leeds:
#     Temperature: 20.0 Celsius
#     Humidity: 55.0%
# (3) average_temperature() that calculates and returns the average temperature from all recorded data in the data_log.
#     If no data is recorded, return None.
# (4) average_humidity() that calculates and returns the average humidity from all recorded data in the data_log. If
#     no data is recoded, return None.

# Additional details:
# (1) Ensure all methods interact seamlessly. For example, record_data should update both the temperature and humidity fields as well
#     as the data_log.
# (2) Include validation of invalid inputs such as out-of-range values for humidity (0-100).
# (3) The average_temperature and average_humidity methods should calculate averages based on data stored in the data_log list.





# Once completed, in a separate file, import this module and create an instance of WeatherStation and
# make at least one calls to each method, preferably with a
# few more calls to record_data.
