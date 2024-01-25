#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics"""
from sys import stdin

fs = -1
sc = -2

if __name__ == "__main__":
    def printstat():
        """Prints the file size and the status codes along with occurences"""
        print("File size:", file_size)
        for key, value in sorted(stat.items()):
            if value:
                print("{}: {}".format(key, value))

    def parselog(file_size):
        """Increments stat and file_size based on contents of line"""
        arr = line.split()
        try:
            file_size += int(arr[fs])
            if arr[sc] in stat:
                stat[arr[sc]] += 1
        except Exception:
            pass
        return file_size

    try:
        file_size = 0
        count = 1
        stat = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
        for line in stdin:
            file_size = parselog(file_size)
            if count % 10 == 0:
                printstat()
            count += 1
        printstat()
    except KeyboardInterrupt:
        printstat()
        raise
