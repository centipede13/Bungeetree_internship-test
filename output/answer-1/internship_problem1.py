import pandas as pd
import argparse
import sys
import os
from time import sleep


def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(description='Group the year by decades and sum the values')
    parser.add_argument('inputDirectory',
                        help='Path to the input directory.')
    parser.add_argument('--outputDirectory',
                        help='Path to the output file.')
    return parser


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.inputDirectory):
        df = pd.read_csv(parsed_args.inputDirectory)

        df.Year = pd.to_datetime(df.Year, format='%Y')
        df.set_index('Year', drop=True, inplace=True)
        df.drop(columns='Total', inplace=True)

        crimes = df.resample('10AS').sum()
        crimes['Population'] = df['Population'].resample('10AS').max()
        crimes2 = crimes.reset_index()
        crimes2['Year'] = crimes2['Year'].dt.year
        if parsed_args.outputDirectory:
            print(parsed_args.outputDirectory)
            crimes2.to_csv(os.path.join(parsed_args.outputDirectory, r'main.csv'))
        print(crimes2)
