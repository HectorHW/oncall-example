# Oncall in docker

This repository contains scripts and config files for setting up Linkedin's oncall service with docker-compose. This project is intended for demonstration purposes.

## Running

Use `docker-compose` in order to build and run services. To create sample users, teams and schedule, install python dependencies with `python -m pip install -r requirements.txt` and execute `setup_schedule.py`

## Configuration

See [config.yaml](config.yaml) for oncall configuration; see appropriate dockerfiles if you wish to change build scripts.
