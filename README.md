# Python PDF Form Filler
Use Python to quickly fill multiple PDF forms. Built for [Coder Kids](https://coder-kids.com/).
This script currently works on a 2 field form with the following input format:
  - A 2 column csv
  - Column headers must match json form fields
  - First column is a single entry
  - Second column is multiple entries separated by commas

Stylistic changes to the PDF can be achieved by editing the PDF's metadata in a program such as Adobe Acrobat DC

## Getting Started
Clone (or download the zip) this repo to use. 

Run the script using this format:
```
./pdf_filler PDF_TO_FILL JSON_FORM_FIELDS OUTPUT_DIRECTORY_NAME
```

Example:
```
./pdf_filler.py seedcert.pdf form_fields.json seed_dummy
```

### Prerequisites
  - Python 3.6+
  - pdfrw ```pip install pdfrw```
  - pandas ```pip install pandas```
  
### 
### Acknowledgments
The write_fillable_pdf function in the pdftools module was adopted from an unknown user's work. Thank you to them!
