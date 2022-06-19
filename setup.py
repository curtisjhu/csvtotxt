from setuptools import setup, find_packages

#when inside venv
#pip install -e . (installs package) as folder
# run `csvtotxt ...`

setup(
    name="csvtotxt",
    version='0.0.1',
    author="Curtis J. Hu",
    author_email="curtis.hu688@gmail.com",
    license="MIT",
    description="Simple tool to build txt files from csv",
    install_requires=[
        'click',
        'colorama'
    ],
    py_modules=[],
    entry_points={
        'console_scripts': [
            'csvtotxt=main.root:cli'
        ]
    }
)