#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rou in range(len(matrix)):
        for numb in range(len(matrix[rou])):
            print("{:d}".format(matrix[rou][numb]), end="")
            if numb != (len(matrix[rou]) - 1):
                print(" ", end="")

        print("")
