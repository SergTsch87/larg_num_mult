#!/usr/bin/env python
# -*- coding: utf-8 -*-

# no copilot

def multiply_str(str_num_1: str, str_num_2: str) -> str:
    return str((ord(str_num_1) - 48) * (ord(str_num_2) - 48))
    # if (len(str_num_1) == 1 and len(str_num_2) == 1):
    #     return str((ord(str_num_1) - 48) * (ord(str_num_2) - 48))
    # else:
    #     return str(int(str_num_1) * int(str_num_2))


def main():
    pass


if __name__ == '__main__':
    main()