<!--
This is the documentation for the AI agent.
It should be comprehensive and detailed.
-->
# Flight Pricer Skill

**Description:**
This skill provides a command-line interface to search for flight options using the Duffel API. It returns a formatted table of flight offers based on user-specified criteria.

**Metadata:**
```yaml
name: flight-pricer
version: 1.0.0
author: J R
requires:
  bins: ["python"]
```

## Setup & Dependencies

The skill is executed via a Python script within a virtual environment.
**Execution Command:** `flight-pricer/.venv/bin/python flight-pricer/flight_pricer.py [COMMAND]`

## Commands

### `config`
Manages the skill's configuration.

#### `config set`
Securely saves the Duffel API key. This is a mandatory first step.

**Usage:**
```bash
flight-pricer/.venv/bin/python flight-pricer/flight_pricer.py config set --api-key <your_api_key>
```

**Arguments:**
-   `--api-key` (string, required): The API key obtained from the Duffel developer dashboard.

---

### `search`
Searches for flight offers based on the provided criteria and displays them in a table.

**Usage:**
```bash
flight-pricer/.venv/bin/python flight-pricer/flight_pricer.py search [OPTIONS]
```

**Arguments:**
-   `--from` (string, required): The IATA code for the departure airport (e.g., `DTW`, `JFK`).
-   `--to` (string, required): The IATA code for the arrival airport (e.g., `MCO`, `LAX`).
-   `--depart` (string, required): The departure date in `YYYY-MM-DD` format.
-   `--return` (string, optional): The return date in `YYYY-MM-DD` format. If provided, the search will be for a round trip.
-   `--passengers` (integer, optional): The number of passengers. Defaults to `1`.
-   `--max-stops` (integer, optional): The maximum number of connections (stops) for the flight. Defaults to `0` (nonstop).
-...
-   `--cabin` (choice, optional): The desired cabin class.
    -   **Allowed values:** `economy`, `business`, `first`, `premium_economy`.

### Examples

**Example 1: One-way, nonstop economy flight for one person.**
```bash
flight-pricer/.venv/bin/python flight-pricer/flight_pricer.py search --from DTW --to MCO --depart 2026-07-20 --cabin economy
```

**Example 2: Round-trip, nonstop, first-class flight for two people.**
```bash
flight-pricer/.venv/bin/python flight-pricer/flight_pricer.py search --from LGA --to MIA --depart 2026-03-27 --return 2026-03-29 --passengers 2 --max-stops 0 --cabin first
```
