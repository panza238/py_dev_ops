"""
Simple tool to measure the execution time of the world timer function
"""
import timeit
import statistics
import sys
import os


# Get the parent directory of the current script
parent_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent of the parent directory
grandparent_dir = os.path.dirname(parent_dir)
# Add the grandparent directory to sys.path
sys.path.append(grandparent_dir)

# This is not the best naming convention
from world_timer.world_timer import world_timer

# Encapsulate all of this in a function to run from main

def wt_timing():
    """
    Measure the execution time of the world_timer function.
    This function executes the world_timer function multiple times and measures the time it takes to execute.
    It performs the following steps:
    1 - SETUP: Initializes a list of cities.
    2 - EXECUTE: Calls the world_timer function multiple times and measures the execution time using the timeit module.
    3 - PRINT: Prints the mean and standard deviation of the execution times.
    """
    # 1 - SETUP
    cities = ['America/Buenos_Aires', 'Europe/London', 'America/Lima', 'America/Los_Angeles', 'Europe/Paris']
    # 2 - EXECUTE
    results = timeit.repeat(lambda: world_timer(cities, quiet=True), repeat=5, number=10)
    # 3 - PRINT
    print(f"Mean: {round(statistics.mean(results), 3)} seconds, Standard Deviation: {round(statistics.stdev(results), 3)} seconds\n")


if __name__ == "__main__":
    wt_timing()
