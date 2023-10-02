#!/usr/bin/python3
"""Reads from stdin line by line & computes metrics"""


def print_stats(size, status_codes):
    """Prints accumulated metrics"""
    print("File size: {:d}".format(size))
    for k in sorted(status_codes):
        print("{}: {:d}".format(k, status_codes[k]))


if __name__ == "__main__":
    import sys

    sz = 0
    stats_codes = {}
    validated_cds = {'200', '301', '400', '401', '403', '404', '405', '500'}
    tally = 0

    try:
        for line in sys.stdin:
            tally += 1

            try:
                elements = line.split()
                code = elements[-2]
                sz += int(elements[-1])

                if code in validated_cds:
                    stats_codes[code] = stats_codes.get(code, 0) + 1
            except (ValueError, IndexError):
                pass

            if tally == 10:
                print_stats(sz, stats_codes)
                tally = 0

    except KeyboardInterrupt:
        print_stats(sz, stats_codes)
        raise
