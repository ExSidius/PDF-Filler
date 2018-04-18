import os
import pdfrw
import csv

# Needed constants for working with pdfrw
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

# Writing to pdf using pdfrw
def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )   
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

# Writing multiple pdfs according to the spreadsheet
def write_pdfs(INPUT_CSV_PATH, TEMPLATE_PATH, col, out_dir):
    field = {}
    num_files = 0 
    with open(INPUT_CSV_PATH, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Get field names
            for c in col:
                field[c] = row[c]
            # Split column 2 names by commas
            courses = row[col[1]].split(',')
            # Each element in column 2
            for c in courses:
                num_files = num_files + 1 
                field[col[1]] = c 
                # Specify output location as out_dir/col1col2.pdf (col2 stopped at :)
                out = row[col[0]].replace(" ", "") + c.replace(" ", "").split(":")[0]
                write_fillable_pdf(TEMPLATE_PATH, out_dir+'/'+ out + '.pdf', field)

    return num_files

