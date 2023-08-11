SHELL=/bin/zsh

# .ONESHELL only works when running gmake. make will ignore it.
.ONESHELL:
.PHONY: clean run logs_setup

all: run clean

poetry.lock:
	poetry install

logs_setup:
	mkdir -p logs

run: logs_setup poetry.lock
	export BASE_WT_LOGS_PATH=$(shell pwd)/logs
	poetry run python world_timer/main.py 

clean: 
	rm -rf __pycache__

# build package source distribution 
dist/*.tar.gz: setup.py world_timer/main.py
	python setup.py sdist
