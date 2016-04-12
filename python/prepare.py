import requests, json
import unicodecsv as csv

# url = "page=%d&maxResults=40&&language=pt&rankingId=0&exactLocation=false&currency=BRL&&



def perform_paged_request(page):
    url = "http://api.vivareal.com/api/1.0/locations/listings"
    params = {
        "apiKey": "183d98b9-fc81-4ef1-b841-7432c610b36e",
        "exactLocation": False,
        "currency": "BRL",
        "business": "RENTA",
        "listingType": "APART",
        "listingUse": "RESIDENCIAL",
        "rankingId":0,
        "locationIds": "BR>Santa Catarina>NULL>Florianopolis",
        "maxResults": 40,
        "page": page
    }

    response = requests.get(url, params=params)
    return json.loads(response.content)

def load_data(out, max  = 100):

    current_page = 1

    data = perform_paged_request(current_page)
    print data
    listings = []

    while current_page < max and data and data["listings"]:
        print current_page
        listings = listings+data["listings"]
        current_page += 1
        data = perform_paged_request(current_page)


    json.dump({"rentals": listings}, open(out, "w"))


load_data("rentals.json")

def toCsv(inputF, outputF):

    rentals = json.load(inputF, encoding="utf-8")["rentals"]
    keys = ["propertyId", "rentPrice", "area", "bathrooms", "rooms",
            "garages", "latitude", "longitude", "address", "suites",
            "rentPeriodId", "condominiumPrice", "iptu"]

    writer = csv.DictWriter(outputF, encoding="utf-8", fieldnames=keys, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows([{k:rental[k] for k in keys} for rental in rentals ])

    # This extracts the extra fields data

    # extraKeys = set().union(*[set(r["additionalFeatures"]) for r in rentals])
    #
    # entries = []
    #
    # print rentals[0]
    #
    # for rental in rentals:
    #     entry = {k: rental[k] for k in keys}
    #     entry.update({k:0 for k in extraKeys})
    #     entry.update({k:1 for k in rental["additionalFeatures"]})
    #     entries += [entry]
    #
    # print keys + list(extraKeys)
    #
    # writer = csv.DictWriter(outputF, encoding="utf-8", fieldnames= keys + list(extraKeys), quoting=csv.QUOTE_ALL)
    #
    # writer.writeheader()
    # writer.writerows(entries)

# load_data("rentals_small.json", max=5)

with open("rentals.json","r") as inputF:
    with open("rentals.csv","w") as outputF:
        toCsv(inputF, outputF)