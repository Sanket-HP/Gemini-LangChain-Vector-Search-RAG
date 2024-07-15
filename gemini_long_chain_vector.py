# Let's extract all code cells from the Jupyter notebook and save them as a .py file.

import nbformat

# Load the Jupyter notebook
with open(file_path, 'r', encoding='utf-8') as file:
    notebook = nbformat.read(file, as_version=4)

# Extract code cells
code_cells = [cell['source'] for cell in notebook.cells if cell.cell_type == 'code']

# Join code cells into a single Python script
script_content = '\n\n'.join(code_cells)

# Define the path for the Python script
script_path = '/mnt/data/gemini_langchain_vector_search_rag.py'

# Save the Python script
with open(script_path, 'w', encoding='utf-8') as script_file:
    script_file.write(script_content)

script_path
