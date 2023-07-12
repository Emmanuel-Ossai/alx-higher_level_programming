#!/usr/bin/python3

"""
Contains a script that reads stdin line by line and computes metrics

"""


import sys
import signal


def compute_metrics():
    """
    Read stdin line by line and compute metrics.
    Print statistics every 10 lines or after a keyboard
    interruption (CTRL + C).

    """
    total_file_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip_address, _, _, status_code, file_size = line.strip().split(' ')

            total_file_size += int(file_size)

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if i % 10 == 0:
                print_stats(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_codes)


def print_stats(total_file_size, status_codes):
    """
    Print the computed statistics

    """
    print("Total file size:", total_file_size)
    for code in sorted(status_codes.keys()):
        print(code + ":", status_codes[code])


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, lambda sig, frame: print_stats(0, {}))

# Call the compute_metrics function
compute_metrics()
