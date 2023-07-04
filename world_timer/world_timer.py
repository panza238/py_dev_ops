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

    response = requests.get(base_url).json()
    return response


def world_timer(cities, verbose=False):
    """CLI tool to list the current time in different cities"""
    if not cities:
        response = list_current_location_time()
        if verbose:
            click.echo("No cities provided. Using current location")
            click.echo(click.style(f"{response['timezone'].split('/')[-1]}: {response['datetime']}", fg='green'))
    else:
        responses = list_cities_time(cities_list=cities)
        if verbose:
            for response in responses:
                click.echo(click.style(f"{response['timezone'].split('/')[-1]}: {response['datetime']}", fg='green'))
            

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
@click.option("--verbose", "-v", is_flag=True, default=False, help="Enable verbose output")
def world_timer_command(cities, verbose):
    """CLI tool to list the current time in different cities"""
    world_timer(cities, verbose)


if __name__ == "__main__":
    world_timer_command()
