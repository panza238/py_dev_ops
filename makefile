
.ONESHELL:
.PHONY: clean run clean logs_setup

all: logs_setup run clean

poetry.lock:
	poetry install

logs_setup:
	mkdir -p logs

poetry_env: poetry.lock
	poetry shell

run: logs_setup poetry_env
	export BASE_WT_LOGS_PATH=$(shell pwd)/logs
	python world_timer/main.py 

clean: poetry_env
	rm -rf __pycache__
	$(shell deactivate)
