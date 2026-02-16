# flight-pricer

A command-line interface (CLI) tool to search for flight prices. This tool is designed to be used as an OpenClaw skill.

## Description

This skill allows a user to query a flight search API (like Duffel) to find flight options based on various criteria such as dates, destinations, number of passengers, and cabin class.

The primary goal is to provide a clean, structured output that can be easily passed to a travel agent for booking.

## Installation & Usage

### Prerequisites
- Python 3.x
- An API key from a flight search provider.

### Setup
1.  **Create and Activate Virtual Environment:**
    ```bash
    # Create the virtual environment
    python3 -m venv .venv

    # Activate it (on macOS/Linux)
    source .venv/bin/activate
    # On Windows, use: .venv\Scripts\activate
    ```

2.  **Install Dependencies:**
    ```bash
    # With the virtual environment active
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    ```bash
    # With the virtual environment active
    python flight_pricer.py config set --api-key <YOUR_API_KEY>
    ```

### Searching for Flights
```bash
# With the virtual environment active
python flight_pricer.py search --from DTW --to MCO --depart 2026-07-20 --passengers 2
```
This will output a summary of the flight search parameters. Full API integration is pending.

## Development Status
This project is in its initial scaffolding phase. The core CLI structure is in place, but it does not yet make live API calls.
