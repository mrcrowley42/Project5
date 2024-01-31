import csv
import json
import os
import sys


"""
This script is intended to convert BOM JSON data in multiple overlapping files in to 
a single CSV with a header that is de-duplicated
At the command line the first argument is the path to the folder containing the inputs
At the command line the second argument is the name of the output CSV file 
Example
python json_to_csv.py "./data_folder" test2.csv 
"""


def write_json_header(file_name_in, file_name_out):
    """
    Output the header of the CSV file from a BOM JSON file
    :param file_name_in:
    :param file_name_out:
    :return:
    """
    if not file_name_in.endswith('.json'):
        return False
    file_to_read = open(file_name_in)
    object_data = file_to_read.read()
    data0 = json.loads(object_data)
    data1 = data0['observations']['data'][0]
    # use the CSV library to output the header of the CSV file
    keys = data1.keys()
    writefile = file_name_out
    with open(writefile, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data1.keys())
    f.close()
    return True


def write_json_data(header_flag_internal, file_name_in, file_name_out):
    """
    Output the data the CSV file from a BOM JSON file
    :param header_flag_internal:
    :param file_name_in:
    :param file_name_out:
    :return: header flag true if the file header was output
    """
    # Guard code
    # Don't want to open a .venv file for example
    if not file_name_in.endswith('.json'):
        return
    # only write the header once
    if not header_flag_internal:
        write_json_header(file_name_in, file_name_out)
        header_flag_internal = True
    file_to_read = open(file_name_in)
    object_data = file_to_read.read()
    data_parent = json.loads(object_data)
    # This is a JSON array
    data = data_parent['observations']['data']
    # use the CSV library to output the header of the CSV file

    writefile = file_name_out
    with open(writefile, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in data:
            # must make the sort order the same or it messes up the duplicate detection
            row['sort_order'] = '999'
            if not duplicated_check(row):
                writer.writerow(row.values())
        f.close()
    return header_flag_internal


def duplicated_check(row):
    """
    Check if the row we are saving is already in the CSV file
    :param row: the row we are going to save
    :return: True if the row we are saving is already in the CSV
    """
    duplicated = row in saved_values
    if not duplicated:
        saved_values.append(row)
    return duplicated


def enumerate_files(path):
    """
    Find the contents of the path. Don't use wildcards. Non JSON files will be ignored
    returns: list of files by name in the folder including those that are not JSON
    """
    # Get the list of all files and directories
    dir_list = os.listdir(path)
    return dir_list


# Only to be run from the command line
if __name__ == '__main__':
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    saved_values = []
    files = enumerate_files(sys.argv[1])
    output_file = sys.argv[len(sys.argv)-1]
    # output the header once
    write_json_header(files[0], output_file)
    # header flag will be written once onl
    header_flag = False
    for file in files:
        if file.endswith('.json'):
            header_flag = write_json_data(header_flag, file, output_file)
