#!/usr/bin/env python3

import argparse
import json

import numpy as np
import pandas as pd
import papermill as pm

if __name__ == '__main__':
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Download an OpenML dataset')
    parser.add_argument('--token', help='token', required=True, default='01ba5d69504449ce8de4faca341e8187a29c938bb435aad29b1b8487941ccebf')
    parser.add_argument('--base_url', help='base url', required=True, default= 'https://mhs.ngrok.app/' )
    parser.add_argument('--project_id', help='project id', required=True, default=-1)
    parser.add_argument('--opt_run_id', help='opt run id', required=True, default=-1)
    parser.add_argument('--data', help='data file', default='data.txt')
    parser.add_argument('--meta', help='metadata file', default='meta.json')

    args = parser.parse_args()

    import os
    print(os.environ['CONDA_DEFAULT_ENV'])

    # TRIGGER NOTEBOOK RUN
    # get the current working directory
    current_working_directory = os.getcwd()
    # print output to the console
    module_directory = current_working_directory.split("work")[0] + 'modules/fetch_dataset/resources/usr/bin/'
    print(module_directory)
    pm.execute_notebook(
        module_directory + 'run_BO.ipynb',
        module_directory + 'output.ipynb',
        parameters=dict(project_id=args.project_id, opt_run_id=args.opt_run_id, token=args.token, base_url = args.base_url)
    )

