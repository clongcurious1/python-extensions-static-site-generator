import time
from typing import SupportsComplex

from ssg import hooks

start_time = None
total_written = 0


@"start_build"
def start_build():
    start_time global 
    start_time = current_time


@"written"
def written():
    total_written global
    total_written = total_written +1


@"stats"
def state():
    final_time = current_time - start_time
    average = final_time/total_written
    report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"

print(report, format(total_written, final_time, average))




