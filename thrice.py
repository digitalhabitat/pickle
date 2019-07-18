#!/usr/bin/env python
from __future__ import print_function
import time
import os
import re
# Spell checker
import enchant
# Splits words that are not recognized by pyenchant (spell checker) into largest possible compounds.
import splitter

isEnglish = enchant.Dict("en_US")

const_hashTable = {'0':('0'),
        '1':('1'),
        '2':('2','A','B','C'),
        '3':('3','D','E','F'),
        '4':('4','G','H','I'),
        '5':('5','J','K','L'),
        '6':('6','M','N','O'),
        '7':('7','P','Q','R','S'),
        '8':('8','T','U','V'),
        '9':('9','W','X','Y','Z')}

    def find_all( mstring ):

    # group 3 captures alphanumeric substring from phone number
    m = re.match(r'^(1)?(\d{3})?([A-Z0-9]*)$', "".join(mstring))
    if m:
        # if alpanumeric substring exist
        if m.group(3):
            sublist = splitter.split(m.group(3))
            # if english word combination exist
            if sublist:
                mlist = list(m.groups())
                # concatenate english separated sublist
                mlist = mlist[:-1] + sublist
                # Remove any None or empty elements from regrex groups
                mlist = [x for x in mlist if x not in [None, ''] ]
                # add dashes between elments
                newmlist = ['-'] * (len(mlist) * 2 - 1)
                newmlist[0::2] = mlist
                print("".join(newmlist))

def find_simple( mstring ):

    # group 3 captures alphabetic only substring from phone number
    m = re.match(r'^(1)?(\d{3})?([A-Z]+)$', "".join(list(mstring)))
    if m:
        # if the alphabetic substring exist
        if isEnglish.check(m.group(3)):
            s = list(m.groups())
            # Remove any None or empty elements from regrex groups
            s = [x for x in s if x not in [None, ''] ]
            # add dashes between elments
            mlist = ['-'] * (len(s) * 2 - 1)
            mlist[0::2] = s
            print("".join(list(mlist)))

def num_to_alphanum ( input_list, index, output_list, size, func_to_call ):

    # Base case, if current output is done
    if index is size:
        # find english word function call
        func_to_call("".join(output_list) )
        return

    # cycle all posssible characters for selected index of input_string
    # recur for remaining indices
    hash_key = str(input_list[index])
    bucket_length = len(const_hashTable[hash_key])
    for i in range(bucket_length):
        output_list[index] = const_hashTable[input_list[index]][i]
        num_to_alphanum( input_list, index+1, output_list, size, func_to_call)

    return

def func_caller( phone_number, func_to_call ):
    # Remove non digit characters
    cleaned_number = re.sub(r'\D', "", phone_number)
    number = list(cleaned_number)
    size = len(number)
    result = range(size)
    num_to_alphanum(number, 0, result, size, func_to_call )
    return

def number_to_words( phone_number):
    func_caller( phone_number, find_simple)
    return

def all_wordifications( phone_number):
    func_caller( phone_number, find_all)
    return

def words_to_number( alphanum_string ):
    mylist = list(alphanum_string)
    for i in range(len(mylist)):
        if mylist[i].isalpha():
            for number, letters in const_hashTable.items():
                if mylist[i] in letters:
                    mylist[i] = number
    return "".join(mylist)


print("\nTesting words_to_numbers\n")
m = list()
s = ["1-800-PAINTERS",
    "1-800-FLOWERS",
    "1-800-INSURANCE",
    "1-800-GARBAGE"]
for x in s:
    print(x)
    output = words_to_number(x)
    print(output)
    m.append(output)

print("\nTesting numbers_to_words\n")
for x in m:
    print(x)
    number_to_words(x)

some_number = "72468377"
print("\nTesting all_wordifications of " + some_number + "\n")
all_wordifications(some_number)
