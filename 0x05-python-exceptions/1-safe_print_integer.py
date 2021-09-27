#!/usr/bin/python3
def safe_print_integer(value):
        try:
                print(int(value))
                return ("{:d}".format(value))
        except:
                return False
