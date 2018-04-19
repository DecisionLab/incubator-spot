#!/bin/python

import datetime
import os
import subprocess
import sys

def run_process(date_stamp, ml_type, tolerance):
    command = "start_oa.py"
    process = subprocess.call(['python', command, '-d', date_stamp, '-t', ml_type, '-l', tolerance])

def main():
    start_date_stamp = sys.argv[1]
    ml_type = sys.argv[2]
    tolerance = sys.argv[3]

    if len(sys.argv) == 5:
        start_date = datetime.datetime.strptime(start_date_stamp,"%Y%m%d")
        end_date = datetime.datetime.strptime(sys.argv[4], "%Y%m%d")
        delta = end_date - start_date
        for x in range (0, delta.days):
            print x
            date_to_run = start_date + datetime.timedelta(days=x)
            new_datestamp = date_to_run.strftime("%Y%m%d")
            run_process(new_datestamp, ml_type, tolerance) 
    else:
         run_process(start_date_stamp, ml_type, tolerance)
        

if __name__ == '__main__':
    main()
