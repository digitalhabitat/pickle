#!/usr/bin/python
import time
import os

# https://www.geeksforgeeks.org/find-possible-words-phone-digits/
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

def num_to_alphanum ( input_list, index, output_list, size ):

    # initial input
    if index is 0:

        print "Finding all alphanumberic combinations for " + "".join(input_list)

    # Base case, if current output is done
    if index is size:
        print "".join(output_list)
        return

    # cycle all posssible characters for selected index of input_string
    # recur for remaining indices
    hash_key = str(input_list[index])
    bucket_length = len(const_hashTable[hash_key])
    # print "hash_key: " + hash_key
    # print "bucket length: " + str(bucket_length)
    for i in range(bucket_length):
        # print "i : " + str(i)
        # print "index: " + str(index)
        # print "hashed index: " + const_hashTable[input_list[index]][i]
        # print (type(const_hashTable[input_list[index]][i]))
        output_list[index] = const_hashTable[input_list[index]][i]
        # print "output_list: " + str(output_list)
        num_to_alphanum( list(number), index+1, output_list, size)


    if input_list[index] is 0 or input_list[index] is 1:
        return

for i in range(10):
    print "index:" + str(i)
    mytuple = const_hashTable[str(i)]
    #print mytuple
    #print "len = " + str(len(mytuple))
    for j in range(len(const_hashTable[str(i)])):
        print const_hashTable[str(i)][j]

number = list("18007246837")
size = len(number)
result = range(size)
num_to_alphanum(number, 0, result, size )
