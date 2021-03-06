# notebook_runner.py

import nbformat
import os

from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(notebook_path):
    nb_name, _ = os.path.splitext(os.path.basename(notebook_path))
    dirname = os.path.dirname(notebook_path)
    
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        
    proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
    proc.allow_errors = True
    
    proc.preprocess(nb, {'metadata': {'path': '/'}})
    output_path = os.path.join(dirname, '{}_all_output.ipynb'.format(nb_name))
    
    with open(output_path, mode='wt') as f:
        nbformat.write(nb, f)
    
if __name__ == '__main__':
    run_notebook('Decorators.ipynb')
