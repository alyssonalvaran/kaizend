# Exercise: Products CSV Reader and Writer

# The main objective of this project idea is to read a CSV with a list
# of products for an ecommerce site. The application should be able to:

# - Prompt the user to specify the filename of the CSV input
# - Use argparse for passing the filename of the CSV input file
# - Remove all products that don’t have categories
# - Output a new CSV file that contains all products
#   that have categories
# - Fix flake8 errors
# - Name the exercise file products_csv_parser.py

import argparse
import sys
import pandas as pd

parser = argparse.ArgumentParser(description="Products CSV Reader and Writer")
parser.add_argument('filename', help='the file to read')

args = parser.parse_args()

print()
print("========================================")
print("Exercise: Products CSV Reader and Writer")
print("========================================")
print()

try:
    df = pd.read_csv(args.filename)
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    print("Removing all products that without categories...\n")
    df = df[df["Categories"].notna()]

    fn_out = args.filename[:-4] + "_mod.csv"
    print("Saving output to " + fn_out + "...\n")
    df.to_csv(fn_out, index=False)

    print("File saved. Bye!\n")
