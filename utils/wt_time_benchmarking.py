"""
Simple tool to measure the execution time of the world timer function
"""
import timeit
import statistics
import sys

# This is not the best naming convention
sys.path.append("/Users/ezequiel.panzarasa/Desktop/Panza/Repos/py_dev_ops")  # PATCH. Just for now
from world_timer.world_timer import world_timer


# Measure the execution time of the world_timer function
# 1 - SETUP
cities = ['America/Buenos_Aires', 'Europe/London', 'America/Lima', 'America/Los_Angeles', 'Europe/Paris']

# 2 - EXECUTE
results = timeit.repeat(lambda: world_timer(cities), repeat=5, number=10)

# 3 - PRINT
print(f"Mean: {statistics.mean(results)}, Standard Deviation: {statistics.stdev(results)}\n")
