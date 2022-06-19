from setuptools import setup, find_packages

setup(
    name="csvtotxt",
    version='0.0.1',
    author="Curtis J. Hu",
    author_email="curtis.hu688@gmail.com",
    license="MIT",
    description="Simple tool to build txt files from csv",
    platforms="me",
    install_requires=[
        'click',
        'colorama'
    ],
    packages=find_packages(
        where=".",
        include=['csvtotxt']
    ),
    entry_points={
        'console_scripts': [
            'csvtotxt=csvtotxt.root:cli'
        ]
    }
)