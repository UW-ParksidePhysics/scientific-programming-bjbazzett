"""
read_two_columns_text
"""

__author__ = "ben_bazzett"

import numpy as np

def read_two_column_data(data):
    try:
        data = np.loadtxt(data).T
        if data.shape[0] != 2:
            raise ValueError("File must contain exactly two columns of data.")
        return data
    except OSError as error:
        raise OSError(f"Could not open file: {data}") from error
    except ValueError as error:
        raise ValueError(f"Invalid file format in: {data}") from error

def main():
    data = 'volumes_energies.dat'
    try:
        data = read_two_column_data(data)
        print(f'{data=}, shape={data.shape}')
    except (OSError, ValueError) as error:
        print(error)

if __name__ == '__main__':
    main()