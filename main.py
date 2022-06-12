import csv
import os
import click

@click.command()
@click.argument("filename")
def cli(filename):
    try:
        csv_file = os.path.abspath(filename)
        txt_file = os.path.splitext(csv_file)[0]+".txt"

        with open(txt_file, 'w+') as output_file:
            with open(csv_file, 'r') as input_file:
                next(input_file)
                [ output_file.write(" ".join(row)+'\n') for row in csv.reader(input_file)]

        output_file.close()

        click.echo(click.style("Success", fg='green'))
        click.echo(click.style(f"result at {txt_file}", fg='blue'))
    except:
        click.echo(click.style("Error occurred. Please check your path", fg='red'), err=True)

if __name__ == "__main__":
    cli()