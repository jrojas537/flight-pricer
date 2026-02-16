import os
import click
import yaml
import requests
import json

CONFIG_DIR = os.path.expanduser("~/.config/flight-pricer")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yaml")
API_BASE_URL = "https://api.duffel.com/air/offer_requests"

def get_api_key():
    """Loads the API key from the config file."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)
            return config.get('api_key')
    except (FileNotFoundError, yaml.YAMLError):
        return None

@click.group()
def cli():
    """A CLI tool to price flights."""
    pass

@cli.group()
def config():
    """Manage the flight-pricer configuration."""
    pass

@config.command()
@click.option('--api-key', 'api_key', required=True, help='Your flight search API key.')
def set(api_key):
    """Sets and saves the API key."""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    config_data = {'api_key': api_key}
    with open(CONFIG_FILE, 'w') as f:
        yaml.dump(config_data, f)
    click.echo(f"Configuration saved to {CONFIG_FILE}")

@cli.command()
@click.option('--from', 'from_iata', required=True, help='Departure airport IATA code.')
@click.option('--to', 'to_iata', required=True, help='Arrival airport IATA code.')
@click.option('--depart', 'depart_date', required=True, help='Departure date (YYYY-MM-DD).')
@click.option('--return', 'return_date', help='Return date for round-trip (YYYY-MM-DD).')
@click.option('--passengers', default=1, type=int, help='Number of passengers.')
@click.option('--max-stops', 'max_connections', default=0, type=int, help='Maximum number of stops (connections).')
@click.option('--cabin', 'cabin_class', type=click.Choice(['economy', 'business', 'first', 'premium_economy']), help='Cabin class.')
def search(from_iata, to_iata, depart_date, return_date, passengers, max_connections, cabin_class):
    """Searches for flight prices with the specified criteria."""
    api_key = get_api_key()
    if not api_key:
        click.echo("API key not found. Please configure it using 'flight-pricer config set --api-key YOUR_KEY'")
        return

    headers = {
        "Accept-Encoding": "gzip",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Duffel-Version": "v2",
        "Authorization": f"Bearer {api_key}"
    }

    slices = [
        {"origin": from_iata, "destination": to_iata, "departure_date": depart_date}
    ]
    if return_date:
        slices.append({"origin": to_iata, "destination": from_iata, "departure_date": return_date})

    passenger_list = [{"type": "adult"}] * passengers

    payload = {
        "data": {
            "slices": slices,
            "passengers": passenger_list,
            "cabin_class": cabin_class,
            "max_connections": max_connections
        }
    }

    # Filter out None values from payload to keep it clean
    if not cabin_class:
        del payload['data']['cabin_class']
    
    click.echo("Sending request to Duffel API...")
    
    try:
        response = requests.post(API_BASE_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        click.echo("--- API Response ---")
        click.echo(json.dumps(response.json(), indent=2))

    except requests.exceptions.HTTPError as err:
        click.echo(f"HTTP Error: {err}")
        click.echo("--- Error Response Body ---")
        try:
            click.echo(json.dumps(err.response.json(), indent=2))
        except json.JSONDecodeError:
            click.echo(err.response.text)
    except requests.exceptions.RequestException as e:
        click.echo(f"An error occurred: {e}")


if __name__ == '__main__':
    cli()
