#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 OTfStB
# Written by Ember
# https://github.com/Emberium/OTfStB


def parse_string(string):
    """
    Gets all unique characters in the string

    :param string: str: Line for processing
    :return: list: A list of unique characters
    """

    resp = []

    for letter in list(string):
        if letter not in resp:
            resp.append(letter)

    return resp


def get_alp_p(count):
    """
    Returns the power of the alphabet

    :param count: int: The number of characters in the alphabet
    :return: int: The power of the alphabet
    """

    for i in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
        if count <= i:
            return i

    raise Exception()


def to_string(integer, bitness):
    """
    Creates a binary symbol

    :param integer: int:
    :param bitness: int: Bitness of alphabet
    :return: str: Binary symbol
    """

    return str(
                bin(integer).lstrip('-0b').zfill(bitness)
               )


def encode(data):
    """
    Gets the amount of information and translates the string into bytes

    :param data: str: The text to be translated
    :return: int: The number of information (bits)
    :return: str: A byte string
    :return: int: The power required of the alphabet
    :return: int: The bitness of the alphabet
    """

    k = len(data)
    letters = parse_string(data)
    power = get_alp_p(
        len(letters)
    )

    i = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096].index(power)

    bin_str = ''

    for item in list(data):
        bin_str += to_string(letters.index(item), i) + " "

    return i*k, bin_str, power, i


if __name__ == '__main__':
    I, binary, pwr, it = encode(
        input('Enter string: ')
    )

    print('Amount of information: %i bit(s)' % I)
    print('The bitness of the alphabet: %i' % it)
    print('The power required of the alphabet: %i' % pwr)
    print('In bytes: %s' % binary)

