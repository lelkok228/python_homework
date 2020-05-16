import json
import sys
import argparse


def read_string(input_file):
    input_string = ''
    if input_file:
        with open(input_file, 'r') as in_:
            input_string = in_.read()
    else:
        for line in sys.stdin:
            input_string += line
    return input_string


def write_string(output_string, output_file):
    if output_file:
        with open(output_file, 'w') as out_:
            out_.write(output_string)
    else:
        print(output_string)


def read_frequency(frequency_file):
    with open(frequency_file, 'r') as freq_file:
        frequency = json.load(freq_file)
    return frequency


def get_alphabet():
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    return alphabet


def encode_caesar(line, key):
    alphabet = get_alphabet()
    res = ''

    for letter in line:
        if letter in alphabet:
            res += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        elif letter.lower() in alphabet:
            res += alphabet[(alphabet.index(letter.lower()) + key) % len(alphabet)].upper()
        else:
            res += letter

    return res


def decode_caesar(line, key):
    alphabet = get_alphabet()

    res = ''
    for letter in line:
        if letter in alphabet:
            res += alphabet[(alphabet.index(letter) - key) % len(alphabet)]
        elif letter.lower() in alphabet:
            res += alphabet[(alphabet.index(letter.lower()) - key) % len(alphabet)].upper()
        else:
            res += letter

    return res


def encode_vigenere(line, key):
    alphabet = get_alphabet()
    key = key.lower()

    res = ''
    for i in range(len(line)):
        if line[i] in alphabet:
            res += alphabet[(alphabet.index(line[i]) + alphabet.index(key[i % len(key)])) % len(alphabet)]
        elif line[i].lower() in alphabet:
            index_line_i_lower = alphabet.index(line[i].lower())
            res += alphabet[(index_line_i_lower + alphabet.index(key[i % len(key)])) % len(alphabet)].upper()
        else:
            res += line[i]

    return res


def decode_vigenere(line, key):
    alphabet = get_alphabet()
    key = key.lower()

    res = ''
    for i in range(len(line)):
        if line[i] in alphabet:
            res += alphabet[(alphabet.index(line[i])) - alphabet.index(key[i % len(key)]) % len(alphabet)]
        elif line[i].lower() in alphabet:
            index_line_i_lower = alphabet.index(line[i].lower())
            res += alphabet[(index_line_i_lower - alphabet.index(key[i % len(key)])) % len(alphabet)].upper()
        else:
            res += line[i]

    return res


def get_frequency(line):
    alphabet = get_alphabet()
    line = line.lower()

    number_of_letters = sum(line.count(letter) for letter in alphabet)
    frequency = {}

    for letter in alphabet:
        if number_of_letters != 0:
            frequency[letter] = line.count(letter) / number_of_letters
        else:
            frequency[letter] = 0

    return frequency


def get_index_of_upper(line):
    index_of_upper = []
    for i in range(len(line)):
    	if line[i].isupper():
    		index_of_upper.append(i)
    return index_of_upper


def hack(line, frequency):
    alphabet = get_alphabet()
    index_of_upper = get_index_of_upper(line)
    line = line.lower()
    number_of_letters = sum(line.count(letter) for letter in alphabet)

    dist = [0] * len(alphabet)
    for shift in range(len(alphabet)):
        new_line = encode_caesar(line, shift)

        for letter in alphabet:
            if number_of_letters != 0:
                dist[shift] += (frequency[letter] - new_line.count(letter) / number_of_letters) ** 2

    res_shift = dist.index(min(dist))
    res_line = encode_caesar(line, res_shift)
    for i in index_of_upper:
    	res_line = res_line[:i] + res_line[i].upper() + res_line[i + 1:]

    return res_line


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode')
    parser.add_argument('--input_file')
    parser.add_argument('--output_file')
    parser.add_argument('--cipher')
    parser.add_argument('--key')
    parser.add_argument('--frequency_file')
    args = parser.parse_args()  

    input_string = read_string(args.input_file)
    if args.frequency_file:
        frequency = read_frequency(args.frequency_file)

    if args.mode == 'encode':
        if args.cipher == 'caesar':
            write_string(encode_caesar(input_string, int(args.key)), args.output_file)
        elif args.cipher == 'vigenere':
            write_string(encode_vigenere(input_string, args.key), args.output_file)

    if args.mode == 'decode':
        if args.cipher == 'caesar':
            write_string(decode_caesar(input_string, int(args.key)), args.output_file)
        elif args.cipher == 'vigenere':
            write_string(decode_vigenere(input_string, args.key), args.output_file)

    if args.mode == 'frequency':
    	write_string(json.dumps(get_frequency(input_string)), args.output_file)

    if args.mode == 'hack':
    	write_string(hack(input_string, frequency), args.output_file)
