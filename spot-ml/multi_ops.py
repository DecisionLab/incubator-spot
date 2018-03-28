mport datetime
import os
import subprocess
import sys

def run_process(date_stamp, ml_type):
    command = "./ml_ops_cdh.sh"
    process = subprocess.call([command, date_stamp, ml_type])

def main():
    start_date_stamp = sys.argv[1]
    ml_type = sys.argv[2]

    if len(sys.argv) == 4:
        start_date = datetime.datetime.strptime(start_date_stamp,"%Y%m%d")
        end_date = datetime.datetime.strptime(sys.argv[3], "%Y%m%d")
        delta = end_date - start_date
        for x in range (0, delta.days):
            date_to_run = start_date + datetime.timedelta(days=x)
            new_datestamp = date_to_run.strftime("%Y%m%d")
            run_process(new_datestamp, ml_type)

    else:
        run_process(start_date_stamp, ml_type)

if __name__ == '__main__':
    main()
