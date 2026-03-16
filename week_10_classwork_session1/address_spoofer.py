
# The 'faker' module is useful if you ever need to create synthetic data for testing
# https://faker.readthedocs.io/en/master/

from faker import Faker   # you may need to 'pip install faker'

import random
import string
import sys

street_name_stubs = [
    "Aberdeen", "Acacia", "Albert", "Alder", "Alexandra", "Ash", "Aspen", "Avon", 
    "Beech", "Birch", "Blossom", "Bridge", "Brook", "Cambridge", "Canal", 
    "Cedar", "Chapel", "Chestnut", "Church", "Clover", "College", "Cornfield", 
    "Crescent", "Cypress", "Daffodil", "Dale", "Deer", "Devon", "Dove", 
    "Elm", "Fallow", "Farm", "Fern", "Field", "Fir", "Flint", "Forest", 
    "Foxglove", "Garden", "Glen", "Green", "Grove", "Hawthorn", "Hazel", 
    "Heather", "Hill", "Holly", "Ivy", "Juniper", "Kingfisher", "Larch", 
    "Lavender", "Lime", "Linden", "Magnolia", "Maple", "Market", "Meadow", 
    "Mill", "Mistletoe", "Oak", "Orchard", "Park", "Pasture", "Peach", 
    "Pear", "Pine", "Poppy", "Primrose", "Queen", "Raven", "River", 
    "Rose", "Rowan", "Sage", "Sand", "School", "Silver", "Snowdrop", 
    "Spring", "St. Andrew", "St. George", "St. John", "St. Mary", 
    "Station", "Stone", "Summer", "Sycamore", "Temple", "Thistle", 
    "Tower", "Tulip", "Valley", "Violet", "Walnut", "Warren", "Water", 
    "Westminster", "Willow", "Woodland"
]

street_name_suffixes = [
    "Avenue", "Boulevard", "Close", "Court", "Crescent", 
    "Drive", "Gardens", "Gate", "Grove", "Hill", 
    "Lane", "Meadow", "Place", "Road", "Square", 
    "Street", "Terrace", "View", "Way", "Walk"
]

cities_postcodes = {
    "Aberdeen": "AB", "Bath": "BA", "Birmingham": "B", "Blackburn": "BB", "Blackpool": "FY",
    "Bolton": "BL", "Bournemouth": "BH", "Bradford": "BD", "Brighton": "BN", "Bristol": "BS",
    "Cambridge": "CB", "Canterbury": "CT", "Cardiff": "CF", "Carlisle": "CA", "Chelmsford": "CM",
    "Chester": "CH", "Coventry": "CV", "Derby": "DE", "Doncaster": "DN", "Durham": "DH",
    "Edinburgh": "EH", "Exeter": "EX", "Glasgow": "G", "Gloucester": "GL", "Guildford": "GU",
    "Hereford": "HR", "Hull": "HU", "Inverness": "IV", "Ipswich": "IP", "Leeds": "LS",
    "Leicester": "LE", "Lincoln": "LN", "Liverpool": "L",
    "Luton": "LU", "Manchester": "M", "Milton Keynes": "MK", "Newcastle upon Tyne": "NE", 
    "Norwich": "NR", "Nottingham": "NG", "Oxford": "OX", "Peterborough": "PE", "Plymouth": "PL",
    "Portsmouth": "PO", "Preston": "PR", "Reading": "RG", "Sheffield": "S", "Shrewsbury": "SY",
    "Slough": "SL", "Southampton": "SO", "St Albans": "AL", "Stoke-on-Trent": "ST", 
    "Swansea": "SA", "Swindon": "SN", "Taunton": "TA", "Telford": "TF", "Truro": "TR", 
    "Wolverhampton": "WV", "Worcester": "WR", "York": "YO"
}

cottage_names = [
    "The Oaks", "The Willows", "Rose Cottage", "Ivy Cottage", "The Gables",
    "Honeysuckle House", "The Old Mill", "The Barn", "The Stables", "Birchwood",
    "Maple Lodge", "Primrose Cottage", "Lilac House", "The Coach House", "Ash Tree Cottage",
    "Cherry Tree House", "The Byre", "The Forge", "The Grange", "The Granary",
    "The Old Rectory", "Pine Lodge", "Meadow View", "Hilltop", "The Firs",
    "The Nook", "Fern Cottage", "The Spinney", "The Vicarage", "The Retreat"
]

## We are going to create a set of fake addresses

# example: python address_spoofer.py fake_address.txt  10

out = sys.argv[1]         # output file name
num = int(sys.argv[2])    # how many?

fake = Faker()

addresses = []

for i in range(num):
    name = fake.name()
    line1 = ""             # randomly choose a house number and street name - use an f-string to format it
    line2 = ""             # randomly choose a city - use an f-string to format it
    postcode = ""          # randomly generate a post-code using the correct city code - use f-strings
                           # post-code structure: 'city-code' + '1 or 2 digits' + 'space' + 'digit' + '2 letters'
    addresses.append([name,line1,line2,postcode])


# write out to file
with open(out, "w") as outf:
    outf.write("name,street,city,postcode\n")
    for each in addresses:
        outf.write(",".join(each)+"\n")

