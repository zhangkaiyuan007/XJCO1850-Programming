import requests

# usage: python random_quote.py

# we will use the API call https://zenquotes.io/api/random for quotes
# you can test this in a browser or with cURL

api_url = "https://zenquotes.io/api/random"

# parse the JSON data to extract the quote
# the key 'q' contains the quote, and 'a' is the author
