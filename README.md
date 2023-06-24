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
4. run the `world_timer.py` script in the `world_timer` directory. Here's an example of how to run the script to
get to the tool's `help` section, from the project's root path:
```bash
python world_timer/world_timer.py --help
```
5. [OPTIONAL] `poetry` offers another way of running this. Instead of activating the virtual environment through `poetry shell`,
you could run it like this: 
```bash
poetry run python world_timer/world_timer.py --help
```
6. Follow the instructions in the `help` section to use the tool!
7. [OPTIONAL] Feel free to play around with `wt_argparse.py` and `wt_fire.py`. These scripts implement the same tool
by using other frameworks (`argparse` and `fire` respectively)
