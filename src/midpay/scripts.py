import click

from midpay.settings import VA_NAME_CHOICES


@click.command()
@click.argument("va_name", type=click.Choice(VA_NAME_CHOICES))
@click.argument("va_number", type=click.STRING)
def cli(va_name, va_number):
    click.echo(va_name)
    click.echo(va_number)
