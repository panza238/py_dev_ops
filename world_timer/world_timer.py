"""
Building the World Timer command with Click
"""
import click
import requests
import datetime
import os


BASE_API_URL = "http://worldtimeapi.org/api/"
BASE_WT_LOGS_PATH = os.environ.get("BASE_WT_LOGS_PATH")


def list_cities_time(cities_list):
    """list provided cities"""
    base_url = BASE_API_URL + "timezone/"

    for city in cities_list:
        response = requests.get(base_url + city)
        click.echo(click.style(f"{city.split('/')[-1]}: {response.json()['datetime']}", fg='green'))


def list_current_location_time():
    """list current location time"""
    base_url = BASE_API_URL + "/ip"

    response = requests.get(base_url).json()
    click.echo("No cities provided. Using current location")
    click.echo(click.style(f"{response['timezone'].split('/')[-1]}: {response['datetime']}", fg='green'))


@click.command()
@click.option('--cities', '-c', multiple=True,
              help="""Select which cities to get the time for. The format MUST be <continent>/<city>\n
              if more than one city is provided, each city must be preceded by the --cities or -c flag\n
              example: -c America/Buenos_Aires -c Europe/London\n
              If no cities are provided, the current location's time will be displayed""")
def world_timer(cities):
    """CLI tool to list the current time in different cities"""
    if not cities:
        list_current_location_time()
    else:
        list_cities_time(cities_list=cities)

    today = datetime.datetime.today().date().isoformat()
    with open(f"{BASE_WT_LOGS_PATH}/log_file_{today}.log", "a") as log_file:
        now = datetime.datetime.now().isoformat()
        log_file.write(f"[{now}] Consulted Cities: {cities}\n")


if __name__ == "__main__":
    world_timer()
