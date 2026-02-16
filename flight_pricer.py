import os
import click
import yaml

CONFIG_DIR = os.path.expanduser("~/.config/flight-pricer")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yaml")

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
@click.option('--max-stops', default=0, type=int, help='Maximum number of stops.')
@click.option('--airline', help='Specific airline IATA code (e.g., DL).')
@click.option('--cabin', type=click.Choice(['economy', 'business', 'first']), help='Cabin class.')
@click.option('--flex-days', default=0, type=int, help='Search +/- N days for flexible dates.')
def search(from_iata, to_iata, depart_date, return_date, passengers, max_stops, airline, cabin, flex_days):
    """Searches for flight prices with the specified criteria."""
    click.echo("--- Flight Search Parameters ---")
    click.echo(f"From: {from_iata} -> To: {to_iata}")
    click.echo(f"Depart: {depart_date}")
    if return_date:
        click.echo(f"Return: {return_date}")
    click.echo(f"Passengers: {passengers}")
    click.echo(f"Max Stops: {max_stops}")
    if airline:
        click.echo(f"Airline: {airline}")
    if cabin:
        click.echo(f"Cabin: {cabin}")
    if flex_days > 0:
        click.echo(f"Date Flexibility: +/- {flex_days} days")
    click.echo("\nNOTE: This is a placeholder. API integration is not yet implemented.")

if __name__ == '__main__':
    cli()
