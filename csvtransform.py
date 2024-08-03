#! /usr/bin/env python3

import sys
import csv
import argparse
import pprint

def transform_csv(input_file, output_file):
    # Open the input CSV file
    with open(input_file, mode='r', newline='', encoding='utf-8-sig') as input_f:
        csv_reader = csv.DictReader(input_f)

        #pprint.pprint(list(csv_reader))
        #sys.exit(0)
        # Define the order of the columns for the output file
        fieldnames = [
                       'Booking Date',
                       'Check Serial Number',
                       'Description',
                       'Debit',
                       'Credit',
                       'Category'
                     ]

        # Open the output CSV file
        with open(output_file, mode='w', newline='') as output_f:
            csv_writer = csv.DictWriter(output_f, fieldnames=fieldnames)

            # Write the header to the output file
            csv_writer.writeheader()

            # Read each row from the input file, rearrange, and write to the output file
            for row in csv_reader:

                if row['Credit Debit Indicator'] == 'Debit':
                    credit = None
                    debit  = row['Amount']
                elif row['Credit Debit Indicator'] == 'Credit':
                    credit = row['Amount']
                    debit  = None

                # Create a new row dictionary with rearranged columns
                transformed_row = {
                    'Booking Date':        row['Booking Date'],
                    'Check Serial Number': row['Check Serial Number'],
                    'Description':         row['Description'],
                    'Debit':               debit,
                    'Credit':              credit,
                    'Category':            row['Category']
                }
                # Write the transformed row to the output file
                csv_writer.writerow(transformed_row)

    print(f"Transformed data has been written to { output_file }")

def main():
    parser = argparse.ArgumentParser(description='Transform CSV data by rearranging columns.')
    parser.add_argument('-i', '--input', required=True, help='Path to the input CSV file')
    parser.add_argument('-o', '--output', required=True, help='Path to the output CSV file')

    args = parser.parse_args()

    transform_csv(args.input, args.output)

if __name__ == "__main__":
    main()

