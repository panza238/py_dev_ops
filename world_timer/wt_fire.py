from typing import Iterable
import fire
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


def world_timer(cities=None):
    """CLI tool to list the current time in different cities
    :param cities: please pass the list of cities like so: Europe/London,Europe/Paris,America/Los_Angeles
    """
    if not cities:
        list_current_location_time()
    else:
        list_cities_time(cities_list=cities.split(','))
        # I could not get Fire to automatically accept a list of cities separated by spaces...


if __name__ == "__main__":
    fire.Fire(world_timer)
