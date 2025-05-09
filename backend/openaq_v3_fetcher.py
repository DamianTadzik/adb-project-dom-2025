import requests
import mysql.connector
from datetime import datetime
import argparse

# Argument parser for command-line credentials
parser = argparse.ArgumentParser(description="Fetch air quality data and store in MySQL DB.")
parser.add_argument("--user", required=True, help="MySQL username")
parser.add_argument("--password", required=True, help="MySQL password")
parser.add_argument("--database", required=True, help="MySQL database name")
parser.add_argument("--apikey", required=True, help="OpenAq api-key")
args = parser.parse_args()

# Konfiguracja połączenia z bazą danych
db = mysql.connector.connect(
    host="mysql.agh.edu.pl",
    port=3306,
    user=args.user,
    password=args.password,
    database=args.database
)
cursor = db.cursor()

# Lista miejsc z których zbieramy dane
id_list = [
    "303989",
    "10659"
]

def get_latest_data(id, apikey):
    url = "https://api.openaq.org/v3/locations"
    params = {
        "locations_id": id
    }
    headers = {
        "X-API-Key": apikey
    }
    r = requests.get(url, params=params, headers=headers)
    r.raise_for_status()
    return r.json()["results"]

results = []
for id in id_list:
    try:
        print(f"Pobieram dane z {id}...")
        data = get_latest_data(id, args.apikey)
        if data:
            results.extend(data)  # albo np. zapisuj do bazy danych
        else:
            print(f"Brak danych dla: {id}")
    except requests.HTTPError as e:
        print(f"Błąd HTTP dla {id}: {e.response.status_code} - {e.response.reason}")
    except Exception as e:
        print(f"Inny błąd dla {id}: {e}")


### DO TEGO MIEJSCA DZIALA JAKOS HEH


def insert_location(city, country, lat, lon):
    cursor.execute("SELECT id FROM locations WHERE city=%s AND country=%s", (city, country))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute(
        "INSERT INTO locations (city, country, latitude, longitude) VALUES (%s, %s, %s, %s)",
        (city, country, lat, lon)
    )
    db.commit()
    return cursor.lastrowid

def insert_measurement(location_id, param, value, unit, time_str):
    time_obj = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
    cursor.execute("""
        INSERT INTO measurements (location_id, parameter, value, unit, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (location_id, param, value, unit, time_obj))
    db.commit()

# # Główna pętla
# data = get_latest_data(CITY, COUNTRY, args.apikey)

# # Grupa lokalizacji wg city-country-lat-lon
# seen_locations = {}

# for row in data:
#     loc_key = (row["city"], row["country"], row["coordinates"]["latitude"], row["coordinates"]["longitude"])
#     if loc_key not in seen_locations:
#         loc_id = insert_location(*loc_key)
#         seen_locations[loc_key] = loc_id
#     else:
#         loc_id = seen_locations[loc_key]
    
#     insert_measurement(
#         loc_id,
#         row["parameter"],
#         row["value"],
#         row["unit"],
#         row["datetime"]
#     )

print("Done.")
