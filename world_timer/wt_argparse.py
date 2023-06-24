"""
Module to illustrate how to create the World Timer CLI tool using argparse
"""

import argparse
import requests

BASE_API_URL = "http://worldtimeapi.org/api/"


def list_cities_time(cities_list):
    """list provided cities"""
    base_url = BASE_API_URL + "timezone/"

    for city in cities_list:
        response = requests.get(base_url + city)
        print(f"{city.split('/')[-1]}: {response.json()['datetime']}")


def list_current_location_time():
    """list current location time"""
    base_url = BASE_API_URL + "/ip"

    response = requests.get(base_url).json()
    print("No cities provided. Using current location")
    print(f"{response['timezone'].split('/')[-1]}: {response['datetime']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="WorldTimer",
        description="Get the time for any city in the world!"
    )
    parser.add_argument('--cities', '-c',
                        metavar='city', nargs="+",
                        help="""Select which cities to get the time for\n
                             The format MUST be <continent>/<city>\n
                             example: America/Buenos_Aires Europe/London""",
                        )
    args = parser.parse_args()

    if not args.cities:
        list_current_location_time()
    else:
        list_cities_time(args.cities)
