#!/usr/bin/python
import time
from pdftools import tools
import os
import argparse
import json

# Parse arguments
# REQUIRED ARGUMENTS
#   - Template pdf to fill
#   - JSON file containing form field names
#   - Input file as a csv (col 1 = field 1, col 2 = field 2 separated by commas)
#   - Output directory name 

parser = argparse.ArgumentParser(description="Fill PDF forms")
parser.add_argument('template')
parser.add_argument('form_fields')
parser.add_argument('input')
parser.add_argument('output')

args = parser.parse_args()

TEMPLATE_PATH = args.template
INPUT_CSV_PATH = args.input

#Define CSV columns/ Form Fields from json file
json_file = args.form_fields

if __name__ == '__main__':

    start_time = time.time()

    # If target directory doesn't exist, make one
    out_dir = args.output
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Load json fields
    with open(json_file, 'r') as f:
        data = json.load(f)


    num_files = tools.write_pdfs(INPUT_CSV_PATH,TEMPLATE_PATH, data['fields'], out_dir)

    # Print the number of pdfs filled and the time it took
    print("---{} PDF files took {} seconds---".format(num_files, (time.time()-start_time)))


