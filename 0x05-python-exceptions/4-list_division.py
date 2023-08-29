#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divres_list = []
    tmp_divres = 0
    for y in range(0, list_length):
        try:
            tmp_divres = my_list_1[y] / my_list_2[y]
        except TypeError:
            tmp_divres = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp_divres = 0
            print("division by 0")
        except IndexError:
            tmp_divres = 0
            print("out of range")
        finally:
            pass
        divres_list.append(tmp_divres)
    return divres_list
