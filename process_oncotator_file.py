import argparse
import csv
import sys

import gvit_categorizers as gvit
import gvit_pathogenicity as pathogenic

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

    description = ("processes Oncotator file, "
                   "requires python {mj}.{mn} or above".format(
                       mj=MIN_VERSION[0], mn=MIN_VERSION[1]))

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

            # and define new fieldnames:
            # yapf: disable
            new_fieldnames = fieldnames + [
                "PVS1",
                "PM1", "PM2", "PM3", "PM4", "PM5", "PM6",
                "PS1", "PS2", "PS3", "PS4",
                "PP1", "PP2","PP3", "PP4", "PP5",
                "BP1", "BP2", "BP3", "BP4", "BP5", "BP6", "BP7",
                "BS1", "BS2", "BS3", "BS4",
                "BA1",
                "Pathogenicity", "PathogenicityRule"
            ]
            # yapf: enable

            row_writer = csv.DictWriter(
                out_f, fieldnames=new_fieldnames, delimiter='\t')
            row_writer.writeheader()

            for data_row in row_reader:
                # yapf: disable
                criteria = {
                    "PVS1": gvit.PVS1(data_row),

                    "PM1": gvit.PM1(data_row),
                    "PM2": gvit.PM2(data_row),
                    "PM3": gvit.PM3(data_row),
                    "PM4": gvit.PM4(data_row),
                    "PM5": gvit.PM5(data_row),
                    "PM6": gvit.PM6(data_row),

                    "PS1": gvit.PS1(data_row),
                    "PS2": gvit.PS2(data_row),
                    "PS3": gvit.PS3(data_row),
                    "PS4": gvit.PS4(data_row),

                    "PP1": gvit.PP1(data_row),
                    "PP2": gvit.PP2(data_row),
                    "PP3": gvit.PP3(data_row),
                    "PP4": gvit.PP4(data_row),
                    "PP5": gvit.PP5(data_row),

                    "BP1": gvit.BP1(data_row),
                    "BP2": gvit.BP2(data_row),
                    "BP3": gvit.BP3(data_row),
                    "BP4": gvit.BP4(data_row),
                    "BP5": gvit.BP5(data_row),
                    "BP6": gvit.BP6(data_row),
                    "BP7": gvit.BP7(data_row),

                    "BS1": gvit.BS1(data_row),
                    "BS2": gvit.BS2(data_row),
                    "BS3": gvit.BS3(data_row),
                    "BS4": gvit.BS4(data_row),

                    "BA1": gvit.BA1(data_row),
                }
                # yapf: enable
                pathogenic_classification = pathogenic.pathogenicity(criteria)

                data_row.update(criteria)
                data_row.update({
                    "Pathogenicity": pathogenic_classification[0],
                    "PathogenicityRule": pathogenic_classification[1],
                })

                row_writer.writerow(data_row)
