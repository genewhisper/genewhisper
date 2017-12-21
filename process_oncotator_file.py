import argparse
import csv
import sys

import gvit_categorizers as gvit

if __name__ == "__main__":
    """
    """

    # check for required python version:
    MIN_VERSION = (3, 6)

    try:
        assert sys.version_info >= MIN_VERSION
    except AssertionError as e:
        print(
            "python < {mj}.{mn} detected.  Update your "
            "environment to >= {mj}.{mn} to continue.".format(
                mj=MIN_VERSION[0], mn=MIN_VERSION[1]),
            file=sys.stderr)
        exit(1)

    description = "processes Oncotator file, requires python 3.6 or above"

    parser = argparse.ArgumentParser(usage=None, description=description)

    parser.add_argument("-i", "--input_file", type=str, required=True)
    parser.add_argument("-o", "--output_file", type=str, required=True)

    args = parser.parse_args()

    print("using input file: {}".format(args.input_file), file=sys.stderr)
    print("using output file: {}".format(args.output_file), file=sys.stderr)

    with open(args.input_file, "r") as in_f:
        with open(args.output_file, "w") as out_f:

            # filter "comment" rows from raw TSV file:
            filtered_rows = filter(lambda x: x[:1] != "#", in_f)

            row_reader = csv.DictReader(filtered_rows, delimiter='\t')

            # get the fieldnames from our row reader:
            fieldnames = row_reader.fieldnames

            # and define new fieldnames to be used by
            # our writer (including the ):
            new_fieldnames = fieldnames + ["PM1", "PVS1", "PM2", "PP3"]

            row_writer = csv.DictWriter(
                out_f, fieldnames=new_fieldnames, delimiter='\t')
            row_writer.writeheader()

            for data_row in row_reader:
                data_row.update({
                    "PM1": gvit.PM1(data_row),
                    "PVS1": gvit.PVS1(data_row),
                    "PM2": gvit.PM2(data_row),
                    "PP3": gvit.PP3(data_row),
                })
                row_writer.writerow(data_row)
