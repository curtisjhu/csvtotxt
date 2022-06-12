# csv_to_txt
Simple CLI tool to build txt files from csv

### If you have trouble turning csv files into txt for Octave as datasets, you're in luck.
Although datasets, such as those on kaggle, are often in csv, Matlab and Octave do not read well in csv. Hence, I've tried to easily convert files reliably into txt files for Octave and Matlab.

### Getting Started
`
git clone https://github.com/curtisjhu/csv_to_txt.git
cd csv_to_txt
pipenv shell
pip install -e .
`
`
csvtotxt example.csv
`

#####TODO
- better installation documentation
- Change strings, or true and false statements...