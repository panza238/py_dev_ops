"""
Building the World Timer command with Click
"""
import click
import requests
import datetime
import os


BASE_API_URL = "http://worldtimeapi.org/api/"
BASE_WT_LOGS_PATH = os.environ.get("BASE_WT_LOGS_PATH", ".")


def list_cities_time(cities_list):
    """list provided cities"""
    base_url = BASE_API_URL + "timezone/"

    response_list = [requests.get(base_url + city).json() for city in cities_list]
    return response_list


def list_current_location_time():
    """list current location time"""
    base_url = BASE_API_URL + "/ip"
    response = [requests.get(base_url).json()]
    # return list for consistency with list_cities_time
    return response


def print_location_time(response):
    """print location time"""
    click.echo(click.style(f"{response['timezone'].split('/')[-1]}: {response['datetime']}",
                           fg="green"))


def world_timer(cities, quiet=False):
    """CLI tool to list the current time in different cities"""

    # if no cities provided, use current location
    if not cities:
        click.echo("No cities provided. Using current location")
        responses = list_current_location_time()
    else:
        responses = list_cities_time(cities_list=cities)

    # If quiet, suppress output to console.
    if quiet:
        pass
    else:
        for response in responses:
            print_location_time(response)

            
    # Log consulted cities
    today = datetime.datetime.today().date().isoformat()
    with open(f"{BASE_WT_LOGS_PATH}/log_file_{today}.log", "a") as log_file:
        now = datetime.datetime.now().isoformat()
        log_file.write(f"[{now}] Consulted Cities: {cities}\n")


@click.command()
@click.option('--cities', '-c', multiple=True,
              help="""Select which cities to get the time for. The format MUST be <continent>/<city>\n
              if more than one city is provided, each city must be preceded by the --cities or -c flag\n
              example: -c America/Buenos_Aires -c Europe/London\n
              If no cities are provided, the current location's time will be displayed""")
@click.option("--quiet", "-q", is_flag=True, default=False, help="quiet mode. Supress output to console")
def world_timer_command(cities, quiet):
    """CLI tool to list the current time in different cities"""
    world_timer(cities, quiet)


if __name__ == "__main__":
    world_timer_command()
