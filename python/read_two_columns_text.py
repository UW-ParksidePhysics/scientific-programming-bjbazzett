"""
read_two_columns_text
"""

__author__ = "ben_bazzett"

import numpy as np

def read_two_column_data(str):
    try:
        data = np.loadtxt(str).T
        if data.shape[0] != 2:
            raise ValueError("File must contain exactly two columns of data.")
        return data
    except OSError as error:
        raise OSError(f"Could not open file: {str}") from error
    except ValueError as error:
        raise ValueError(f"Invalid file format in: {str}") from error

def main():
    str = 'volumes_energies.dat'
    try:
        data = read_two_column_data(str)
        print(f'{data=}, shape={data.shape}')
    except (OSError, ValueError) as error:
        print(error)

if __name__ == '__main__':
    main()