import csv
import os
import click
from .pandas import dropna, fillna, remove_duplicates, script

@click.group()
@click.command()
@click.argument("filename")
def cli(filename):
    try:
        csv_file = os.path.abspath(filename)
        txt_file = os.path.splitext(csv_file)[0]+".txt"

        with open(txt_file, 'w+') as output_file:
            with open(csv_file, 'r') as input_file:
                reader = csv.reader(input_file)
                header = next(reader)
                [ output_file.write(" ".join(row)+'\n') for row in reader ]

        output_file.close()

        click.echo(click.style("Success", fg='green'))
        click.echo(click.style(f"result at {txt_file}", fg='blue'))
    except:
        click.echo(click.style("Error occurred. Please check your path", fg='red'), err=True)



cli.add_command(script)
cli.add_command(remove_duplicates)
cli.add_command(dropna)
cli.add_command(fillna)

if __name__ == "__main__":
    cli()