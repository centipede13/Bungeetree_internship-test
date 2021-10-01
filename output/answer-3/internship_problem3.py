import pandas as pd
import argparse
import sys
import os


def create_arg_parser():
    # Creates and returns the ArgumentParser object

    parser = argparse.ArgumentParser(
        description=' Sorting the teams by Red Cards, then to Yellow Cards')
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
        df2 = df[['Team', 'Yellow Cards', 'Red Cards']]

        df_res = df2.sort_values(
            ['Red Cards', 'Yellow Cards'], ascending=False)

        if parsed_args.outputDirectory:
            print(parsed_args.outputDirectory)
            df_res.to_csv(os.path.join(
                parsed_args.outputDirectory, r'main.csv'))

        print(df_res)
