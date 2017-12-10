

import argparse
import csv
import sys

from gvit_categorizers import PM1 as pm1_flag


if __name__ == "__main__":
    """
    """

    description = "processes Oncotator file"

    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-i", "--input_file", type=str)
    parser.add_argument("-o", "--output_file", type=str)

    args = parser.parse_args()

    
    print("using input file: {}".format(args.input_file),
          file=sys.stderr)
    print("using output file: {}".format(args.output_file),
          file=sys.stderr)

    
    with open(args.input_file, "r") as in_f:
        with open(args.output_file, "w") as out_f:

            # filter "comment" rows from raw TSV file:
            filtered_rows = filter(lambda x: x[:1] != "#", in_f)

            row_reader = csv.DictReader(filtered_rows, delimiter='\t')

            # get the fieldnames from our row reader:
            fieldnames = row_reader.fieldnames

            # and define new fieldnames to be used by
            # our writer (including the ):
            new_fieldnames = fieldnames + ["PM1"]

            row_writer = csv.DictWriter(out_f,
                                        fieldnames=new_fieldnames,
                                        delimiter='\t')
            row_writer.writeheader()
            
            for data_row in row_reader:
                data_row.update({
                    "PM1": pm1_flag(data_row)                    
                })
                row_writer.writerow(data_row)
                
