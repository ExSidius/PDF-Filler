import time
from pdftools import tools
import os
import json
import pandas as pd
import datetime

# Helper functions

def process_status(x):
    """
    Function that processes TalentLMS's status output.
    """

    if x == 'Completed':
        return 100
    elif x == 'Not started':
        return -1
    else:
        return round(x * 100)

def get_names():
    """
    Get list of names from input csv.
    """

    return list(pd.read_csv('input.csv')['Name'])

def generate_input():
    df = pd.read_excel('data.xlsx', header=3)
    df = df.rename(index=str, columns={'Status': 'Status (%)'})

    df['Name'] = df.apply(lambda row : row['First name'] + ' ' + row['Last name'], axis=1) # Create name column.
    df = df.drop(['First name', 'Last name', 'Email', 'Enrolled on', 'Time', 'Completion date'], axis=1) # Drop useless columns.

    df['Status (%)'] = df['Status (%)'].apply(process_status) # Process status columns.

    df_new = pd.DataFrame() # Create new dataframe.

    for name in get_names():
        df_new = pd.concat([df_new, df[(df['Name'] == name) & (df['Status (%)'] >= 80)]])

    df_new = df_new[['Name', 'Course', 'Status (%)']]

    df_new.to_csv('temp.csv')

# Parse arguments
# REQUIRED ARGUMENTS
#   - Template pdf to fill
#   - JSON file containing form field names
#   - Input file as a csv (col 1 = field 1, col 2 = field 2 separated by commas)
#   - Output directory name

TEMPLATE_PATH = './seedcert.pdf'
INPUT_CSV_PATH = './temp.csv'
OUT_DIR = 'seed_' + str(datetime.datetime.today())
JSON_FILE = './form_fields.json'

if __name__ == '__main__':

    generate_input()

    start_time = time.time()


    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    # Load json fields
    with open(JSON_FILE, 'r') as f:
        data = json.load(f)


    num_files = tools.write_pdfs(INPUT_CSV_PATH,TEMPLATE_PATH, data['fields'], OUT_DIR)

    # Print the number of pdfs filled and the time it took
    print("---{} PDF files took {} seconds---".format(num_files, (time.time()-start_time)))

    os.remove('temp.csv')

