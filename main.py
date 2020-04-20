import json
import sys


def read_s(in_file):
    res = ''
    if in_file == 'console':
        for line in sys.stdin:
            res += line
    else:
        with open(in_file, 'r') as in_:
            res = in_.read()
    return res


def write_s(s, out_file):
    if out_file == 'console':
        print(s)
    else:
        with open(out_file, 'w') as out_:
            out_.write(s)


def encode_caesar(key, in_file, out_file):
    global alphabet

    s = read_s(in_file)

    res = ''
    for i in s:
        if i in alphabet:
            res += alphabet[(alphabet.index(i) + key) % len(alphabet)]
        elif i.lower() in alphabet:
            res += alphabet[(alphabet.index(i.lower()) + key) % len(alphabet)].upper()
        else:
            res += i

    write_s(res, out_file)


def decode_caesar(key, in_file, out_file):
    global alphabet

    s = read_s(in_file)

    res = ''
    for i in s:
        if i in alphabet:
            res += alphabet[(alphabet.index(i) - key) % len(alphabet)]
        elif i.lower() in alphabet:
            res += alphabet[(alphabet.index(i.lower()) - key) % len(alphabet)].upper()
        else:
            res += i

    write_s(res, out_file)


def encode_vigenere(key, in_file, out_file):
    global alphabet

    key = key.lower()
    s = read_s(in_file)

    res = ''
    for i in range(len(s)):
        if s[i] in alphabet:
            res += alphabet[(alphabet.index(s[i]) + alphabet.index(key[i % len(key)])) % len(alphabet)]
        elif s[i].lower() in alphabet:
            res += alphabet[(alphabet.index(s[i].lower()) + alphabet.index(key[i % len(key)])) % len(alphabet)].upper()
        else:
            res += s[i]

    write_s(res, out_file)


def decode_vigenere(key, in_file, out_file):
    global alphabet

    key = key.lower()
    s = read_s(in_file)

    res = ''
    for i in range(len(s)):
        if s[i] in alphabet:
            res += alphabet[(alphabet.index(s[i]) - alphabet.index(key[i % len(key)])) % len(alphabet)]
        elif s[i].lower() in alphabet:
            res += alphabet[(alphabet.index(s[i].lower()) - alphabet.index(key[i % len(key)])) % len(alphabet)].upper()
        else:
            res += s[i]

    write_s(res, out_file)


def count_frequency(in_file, out_file):
    global alphabet

    s = read_s(in_file)
    s = s.lower()

    number_of_letters = sum(s.count(i) for i in alphabet)
    frequency = {}

    for i in alphabet:
        if number_of_letters != 0:
            frequency[i] = s.count(i) / number_of_letters
        else:
            frequency[i] = 0

    write_s(json.dumps(frequency), out_file)


def hack(in_file, out_file, frequency_file):
    global alphabet

    s = read_s(in_file)

    number_of_letters = 0
    ind_of_upper = []
    for i in range(len(s)):
        if s[i].lower() in alphabet:
            number_of_letters += 1
        if s[i].isupper():
            ind_of_upper.append(i)
    s = s.lower()

    with open(frequency_file, 'r') as freq_file:
        freq = json.load(freq_file)

    dist = [0] * len(alphabet)
    for shift in range(len(alphabet)):
        new_s = ''
        for i in s:
            if i in alphabet:
                new_s += alphabet[(alphabet.index(i) + shift) % len(alphabet)]
            else:
                new_s += i

        for i in alphabet:
            if number_of_letters != 0:
                dist[shift] += (freq[i] - new_s.count(i) / number_of_letters) ** 2

    res_shift = dist.index(min(dist))
    res = ''
    for i in range(len(s)):
        if s[i] in alphabet:
            if i in ind_of_upper:
                res += alphabet[(alphabet.index(s[i]) + res_shift) % len(alphabet)].upper()
            else:
                res += alphabet[(alphabet.index(s[i]) + res_shift) % len(alphabet)]
        else:
            res += s[i]

    write_s(res, out_file)


if __name__ == '__main__':
    alphabet = []
    for i in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(i))

    if sys.argv[1] == 'encode':
        if sys.argv[2] == 'caesar':
            encode_caesar(int(sys.argv[3]), sys.argv[4], sys.argv[5])
        elif sys.argv[2] == 'vigenere':
            encode_vigenere(sys.argv[3], sys.argv[4], sys.argv[5])

    if sys.argv[1] == 'decode':
        if sys.argv[2] == 'caesar':
            decode_caesar(int(sys.argv[3]), sys.argv[4], sys.argv[5])
        elif sys.argv[2] == 'vigenere':
            decode_vigenere(sys.argv[3], sys.argv[4], sys.argv[5])

    if sys.argv[1] == 'frequency':
        count_frequency(sys.argv[2], sys.argv[3])

    if sys.argv[1] == 'hack':
        hack(sys.argv[2], sys.argv[3], sys.argv[4])
