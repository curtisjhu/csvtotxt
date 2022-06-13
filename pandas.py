import sys
import pandas as pd
import click
import os

@click.command()
@click.argument("filename", type=click.File("csv"))
@click.option("-v", "--value", "value")
@click.option("-c", "--column", "column", multiple=True)
@click.option("--stat", "stat", type=click.Choice(['mean', 'mode', 'median']), case_sensitive=False)
def fillna(filename, value, column, stat):
    path = os.path.abspath(filename)
    df = pd.read_csv(path)

    if not value and not stat:
        click.prompt("Replace N/A with value: ")

    if column:
        for col in column:
            value = stat and eval(f"df[col].{stat}()")
            df[col].fillna(value, inplace = True)
    else:
        df.fillna(value, inplace = True)
    
    df.to_csv(path)


@click.command()
@click.argument("filename", type=click.File("csv"))
@click.option("--axis", click.Choice(['index, column, 0, 1']), case_sensitive=False)
@click.option("--subset", multiple=True)
def dropna(filename, axis, subset):
    path = os.path.abspath(filename)
    df = pd.read_csv(path)

    axis = axis if axis else 0
    subset = subset if subset else []

    df.dropna(axis=axis, subset=subset, inplace=True)

@click.command()
@click.argument("filename", type=click.File("csv"))
def remove_duplicates(filename):
    path = os.path.abspath(filename)
    df = pd.read_csv(path)
    df.drop_duplicates(inplace = True)


@click.command()
@click.argument("filename", "name of csv file", type=click.File("csv"))
@click.argument("script", "running small piece of software", type=click.File("py"))
def script(filename, script):
    path = os.path.abspath(filename)
    df = pd.read_csv(path)


    sys.exec("")

