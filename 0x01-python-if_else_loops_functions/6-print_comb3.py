#!/usr/bin/python3
nmb = 0
while nmb <= 89:
    if nmb % 10 == 0:
        nmb += 1 + nmb // 10
    print("{:02d}".format(nmb), end=', ' if nmb != 89 else "\n")
    nmb += 1
