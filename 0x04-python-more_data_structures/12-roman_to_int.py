#!/usr/bin/python3


def calculate_subtraction(list_num):
    max_list = max(list_num)
    to_sub = sum(filter(lambda n: max_list > n, list_num))
    return max_list - to_sub


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        if ch in rom_n:
            if rom_n[ch] <= last_rom:
                num += calculate_subtraction(list_num)
                list_num = [rom_n[ch]]
            else:
                list_num.append(rom_n[ch])

            last_rom = rom_n[ch]

    num += calculate_subtraction(list_num)

    return num
