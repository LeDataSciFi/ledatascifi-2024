'''
Use 1: Edit the text of an entire jupyterbook is a PITA. 

My plan:
1. This file combines all markdown content in the book (text) into one long 
   ipynb file, and then converts that into a Word file using pandoc.
2. Open the word file and let grammarly do the work to find issues!

Use 2: Edit the text of several ipynb files (but not the whole book). This
is valuable when adding or tweaking some pages but a full book edit is not 
necessary.

    (not implemented yet)
    
    1. new input: only_these = None or list of pages
    
    2. if only_these:
        convert_these = [s for s in convert_these if s in only_these]
    

'''

# We will look here for textbook files
directory = 'C:/Users/DonsLaptop/Desktop/GitHub/ledatascifi-2024/content/' 

# skip files with these strings in the path
filters = ['old ', 'ipynb_checkpoint']

# Produce this file
out_doc = 'jupyter_book_to_edit.docx'

import nbformat, os, subprocess

def extract_markdown_cells(nb):
    # This is used to extract all markdown cells in an ipynb file.
    cells = []
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            cells.append(cell)
    return cells

def markdown_to_cell(markdown_filename):
    # This is used to convert a .md file to a ipynb cell.
    with open(markdown_filename, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    cell = nbformat.v4.new_markdown_cell(markdown_text)
    return cell

def combine_markdown_cells(markdown_cells):
    # Convert a list of markdown cells to a ipyn notebook
    combined_nb = nbformat.v4.new_notebook()
    for cell in markdown_cells:
        combined_nb.cells.append(cell)
    return combined_nb

# assemble list of files to convert

convert_these = []   
for root, dirs, files in os.walk(directory):
  for file in files:
    if file.endswith('.ipynb') or file.endswith('.md'):
      convert_these.append(os.path.join(root, file))

convert_these = [s for s in convert_these if not any(f in s for f in filters)] 

# extract markdown from all

markdown_cells = []
for filename in convert_these:
    header = f'# FILENAME: {os.path.basename(filename)}'
    header_cell = nbformat.v4.new_markdown_cell(header)
    markdown_cells.append(header_cell)

    if filename[-3:] == '.md':
        markdown_cells.append(markdown_to_cell(filename))
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            nb = nbformat.reads(f.read(), as_version=4)
            markdown_cells.extend(extract_markdown_cells(nb))

# output comined ipynb

combined_nb = combine_markdown_cells(markdown_cells)

with open('temp.ipynb', 'w', encoding='utf-8') as f:
    f.write(nbformat.writes(combined_nb))

# convert ipynb to docx

if os.path.exists(out_doc):
    os.remove(out_doc)

result = subprocess.run(['pandoc', 'temp.ipynb', '-s', '-o', out_doc])
if result.returncode == 0:
    print('Conversion successful!')
else:
    print('Conversion failed with error code', result.returncode)

os.remove('temp.ipynb')

