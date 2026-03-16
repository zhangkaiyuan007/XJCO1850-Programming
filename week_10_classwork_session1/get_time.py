import requests
import sys

# free Time api https://timeapi.io/swagger/index.html
# timezone info can be found at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# usage: python get_time.py <timezone>

api_url = "https://timeapi.io/"

timezone = sys.argv[1]


# make the correct api call and extract the current time in that timezone

# example python get_time.py Asia/Kuala_Lumpur
