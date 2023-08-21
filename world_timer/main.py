"""
Building the World Timer command with Click
"""
import click
import requests
import datetime
import os
import logging
from logging.handlers import TimedRotatingFileHandler


# CONSTANTS
BASE_API_URL = "http://worldtimeapi.org/api/"
BASE_WT_LOGS_PATH = os.environ.get("BASE_WT_LOGS_PATH", ".")
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)


# LOGGING CONFIGURATION
logging_extra = {"app_name": "world-timer"}

# Create logger
logger = logging.getLogger(name=__name__)
logger.setLevel(LOG_LEVEL)
# Create handler & formatter for logger
file_handler = TimedRotatingFileHandler(
    BASE_WT_LOGS_PATH + f"/world-timer.log",
    when='D', interval=1)
file_format = logging.Formatter(fmt='%(asctime)s - %(app_name)s - %(levelname)s - %(message)s',
                                datefmt='%d/%m/%Y %H:%M:%S')

file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)


# WORLD_TIMER CODE

def list_cities_time(cities_list):
    """list provided cities"""
    base_url = BASE_API_URL + "timezone/"

    response_list = [requests.get(base_url + city).json() for city in cities_list]
    for response in response_list:
        if 'error' in response:
            logger.error(f"Error: {response['error']}", extra=logging_extra)

    return response_list


def list_current_location_time():
    """list current location time"""
    base_url = BASE_API_URL + "/ip"
    response = [requests.get(base_url).json()]
    # return list for consistency with list_cities_time
    return response


def print_location_time(response):
    """print location time"""
    try:
        click.echo(click.style(f"{response['timezone'].split('/')[-1]}: {response['datetime']}",
                           fg="green"))
    except KeyError:
        click.echo(click.style(f"Error: {response['error']}", fg="red"))


def world_timer(cities, quiet=False):
    """CLI tool to list the current time in different cities"""

    logger.info(f"Starting World Timer", extra=logging_extra)

    # if no cities provided, use current location
    if not cities:
        click.echo("No cities provided. Using current location")
        responses = list_current_location_time()
        logger.info(f"No cities provided. Using current location\n", extra=logging_extra)
    else:
        responses = list_cities_time(cities_list=cities)
        logger.info(f"Consulted Cities: {cities}\n", extra=logging_extra)

    # If quiet, suppress output to console.
    if quiet:
        pass
    else:
        for response in responses:
            print_location_time(response)


# WORLD TIMER COMMAND

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
