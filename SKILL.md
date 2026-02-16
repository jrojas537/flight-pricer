# SKILL.md for flight-pricer

name: flight-pricer
description: A CLI tool to search for flight prices using a flight search API.
author: jrojas537@gmail.com
version: "0.1.0"

metadata:
  requires:
    bins: ["python3"]
    pips: ["click", "requests", "pyyaml"]

usage: |
  The main entrypoint for the skill is the `flight-pricer` command.

  **NOTE:** This skill is under active development.

  ## Configure the API Key

  You must configure the skill with a valid API key from the chosen provider (e.g., Duffel).

  `flight-pricer/.venv/bin/python flight_pricer.py config set --api-key <YOUR_API_KEY>`

  ## Search for Flights

  Search for flight options with flexible parameters.

  `flight-pricer/.venv/bin/python flight_pricer.py search --from <IATA_CODE> --to <IATA_CODE> --depart <YYYY-MM-DD> [options]`

  ### Search Options
  * `--return <YYYY-MM-DD>`: For round-trip searches.
  * `--passengers <COUNT>`: Number of passengers (default: 1).
  * `--max-stops <COUNT>`: Maximum number of stops (default: 0).
  * `--airline <IATA_CODE>`: Specify an airline (e.g., 'DL' for Delta).
  * `--cabin <CLASS>`: 'economy', 'business', 'first'.
  * `--flex-days <NUMBER>`: Search +/- days around the departure/return dates.
