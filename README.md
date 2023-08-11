# Python for DevOps
The idea is to develop a simple project based on the book Python for DevOps by Alfredo Deza and Noah Gift.
The project will consist of a simple CLI tool that gets the time for any given city. This should provide a simple
enough platform to build around, using the tools presented in the book.

## Getting Started
This project's dependencies are managed through `poetry`.<br>
If you already have `poetry` up and running in your setup, you should be good to go by simply running 
`poetry install`.<br>
Otherwise, there is a great intro to setting up `poetry` [here](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
The whole series is worth a read, but the first chapter should be enough to run this project. I have found the 
combination of `pipx` and `pyenv` to be the best, but feel free to experiment with other setups<br>
Also, [here](https://python-poetry.org/docs/#installing-with-pipx) you will find poetry's official documentation on 
how to install with `pipx`

## WorldTimer CLI tool
WorldTimer is a CLI tool that allows the user to get the time for any city in the world!
Why google the local time of a city when you can use this tool? 
(yes... that is suposed to be read with a hint of irony)

### Usage
1. Install the project with `poetry` (see *Getting Started* section above)
2. Define where you want to keep the logs by setting the environment variable `BASE_WT_LOGS_PATH` like so:
```bash
export BASE_WT_LOGS_PATH=<path to your logs directory>
```
*If you ommit this step, the current working directory will be used to store logs*
3. run `poetry shell` to activate the virtual environment provided by poetry
    *(`poetry shell` actually spawns a **new** shell withinh the virtual environment. A subtle, but sometimes important, difference)*
4. run the `main.py` script in the `world_timer` directory. Here's an example of how to run the script to
get to the tool's `help` section, from the project's root path:
```bash
python world_timer/main.py --help
```
5. [OPTIONAL] `poetry` offers another way of running this. Instead of activating the virtual environment through `poetry shell`,
you could run it like this: 
```bash
poetry run python world_timer/main.py --help
```
6. Follow the instructions in the `help` section to use the tool!
7. [OPTIONAL] Feel free to play around with `wt_argparse.py` and `wt_fire.py`. These scripts implement the same tool
by using other frameworks (`argparse` and `fire` respectively)

## Utils
In the `utils` directory, you will find two tools used for load testing: `load_test_ab.py` and `load_test_molotov.py`

**WARNING!** These tools might overload a server if not used correctly. Be careful when choosing the arguments. 

### AB tool
The `load_test_ab.py` script allows you to run a simple load test by using the `ab` CLI tool. You can run it like this:
```bash
python load_test_ab.py --help
```
By following the example in the tool's `help` menu, you should be able to run a simple load test.

### Molotov tool
The `load_test_molotov.py` script allows you to run a simple load test by using the `molotov` library. You can run it like this:
1. Make sure you have the poetry virtual environment activated. You can do this by running `poetry shell`
2. Run `molotov` like this (assuming you are in the project's root directory):
```bash
molotov -d 5 utils/load_test_molotov.py
```
This will run the load tests specified in the `utils/load_test_molotov.py` script for 5 seconds. The current tests 
are designed to fail about 20% of the time, so expect a few failures.
3. [OPTIONAL] I have found it difficult to capture the output of the tool. What worked best for me was to direct the
the output to a log file like this:
```bash
molotov -d 5 utils/load_test_molotov.py > <path_to_log_file>
```
`molotov` has many CLI options you can play around. 
[Here's a link to the documentation](https://molotov.readthedocs.io/en/stable/cli/) describing what each of them does.


### Time benchmarking
IN the utils directory, you will find a script called `wt_time_benchmarking.py`. This script allows you to run
a simple performance test. This tool is based on the Python `timeit` module.<br>
**How to run:**
1. Make sure you have the poetry virtual environment activated. You can do this by running `poetry shell`
    *(`poetry shell` actually spawns a **new** shell withinh the virtual environment. A subtle, but sometimes important, difference)*
2. run `python utils/wt_time_benchmarking.py`

## PYTHONSTARTUP
The aim of this section is to customize the Python shell.
To make the functions and methods defined in `utils/python_startup.py` available in every Python REPL, you must first
set the `PYTHONSTARTUP` environment variable like this (assuming you are in the project's root directory):
```bash
export PYTHONSTARTUP=./utils/python_startup.py
```


## Makefile 
In the `makefile` there are a few useful recipes. 
If you are running this on a MacOS system, I recommend you use `gmake` instead of `make`. (`gmake` can be installed with `homebrew`)
**How to run:**
```bash
gmake <target>
```
See makefile for available targets.
if no target is specified, the default target is `all`.
