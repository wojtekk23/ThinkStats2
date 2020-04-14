"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

import gzip
import pandas as pd


def get_colspecs(data_dict):
    half_intervals = []
    running_a = 0

    for [_, _, length] in data_dict:
        half_intervals.append([running_a, running_a+length])
        running_a += length

    return half_intervals


def ReadFemResp():
    raw_data = get_raw_data()
    data_dict = read_stat_dict()

    # df = parse_raw_data(raw_data, data_dict)
    # XDDDDDDDDDD
    df = pd.read_fwf('2002FemPreg.dat.gz', colspecs=get_colspecs(data_dict), copmression='gzip')
    df.set_axis([key for [key, _, _] in data_dict], axis=1, inplace=True)

    return df

def get_raw_data(data_file='2002FemPreg.dat.gz', compression='gzip'):
    if compression is 'gzip':
        f = gzip.open(data_file, 'rb')
        content = f.read()
        f.close()

        return content.splitlines()
    else:
        raise Exception("Can't you have gzip data, please?")

def read_stat_dict(dict_name='2002FemPreg.dct'):
    d = []

    dict_file = open(dict_name, 'r')
    lines = dict_file.readlines()

    for line in lines[1:-1]:
        tokens = line.split()

        d.append([tokens[2], tokens[1], int(tokens[3][1:-1])])

    return d

def parse_raw_data(raw_data, data_list):
    df = pd.DataFrame(columns=[v for [v, _, _] in data_list])

    for record in raw_data:
        row_dict = {}
        running_idx = 1

        for [column, dtype, form] in data_list:
            val_string = record[running_idx:running_idx+form]

            val = np.nan
            try:
                if dtype == "str12":
                    # To tak naprawdę duża liczba całkowita
                    val = int(val_string)
                elif dtype == "int":
                    val = int(val_string)
                elif dtype == "byte":
                    val = int(val_string)
                elif dtype == "float":
                    val = float(val_string)
                elif dtype == "double":
                    val = float(val_string)
            except ValueError:
                val = np.nan

            row_dict[column] = val
            running_idx += form

        df = df.append(row_dict, ignore_index=True)

    return df





def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    print(ReadFemResp())

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)



