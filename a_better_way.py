#!/usr/bin/python
import time
import os
import re
# Spell checker
import enchant
# Splits words that are not recognized by pyenchant (spell checker) into largest possible compounds.
import splitter

isEnlish = enchant.Dict("en_US")



THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
absolute_path_2_file = os.path.join(THIS_FOLDER, 'wordlist.txt')
try:
    myfile = open("output.txt", "w+")
except OSError:
    try:
        os.remove("output.txt")
    except OSError:
        f = open("output.txt", "r")
#absolute_path_2_file = os.path.join(THIS_FOLDER, 'output.txt')

# https://www.geeksforgeeks.org/find-possible-words-phone-digits/

# catdogfish
# 2283643474

# coolpets
# 26657387
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

    singleword = 1;
    minwordsize = 3;
    # initial input
    if index is 0:

        print "Finding all alphanumberic combinations for " + "".join(input_list)


    # Base case, if current output is done
    if index is size:
        # matching
        # 1st group:
        #   and optional group of (at least 1 or more digits) followed by
        #   if condition is met:
        #       a group of (at least 1 or more uppercase characters)
        #   if condition is not met:
        #       group of (at least 1 or more uppercase characters)
        # tldr;
        #   case1: 1 or more uppper case characters
        #   case2: 1 or more numbers followed by 1 or more upppercase case characters
        #   matching group 2 captures the all characters from [A-Z]
        # astring =  "".join(output_list)
        # if len(splitter.split(astring)) > 1:
        #     print astring
        #     for lines in astring:
        #         print lines
        this = splitter.split("".join(output_list))
        if this:
            #print "".join(this)
            #for splits in this:
            ##print splits
            mlist = ['-'] * (len(this) * 2 - 1)
            mlist[0::2] = this
            print "".join(mlist)
        m =  re.match(r'^(\d+)?(?(1)([A-Z]+)|([A-Z]+))$',"".join(output_list),re.IGNORECASE)
        if m:
            #print m.group()
            mystring = m.group(2)

            if m.group(2) is None:
                if m.group(1) is not None:
                        print m.group(1)
                else:
                    return
            elif len(str(m.group(2))) > 2:
                #print m.group()
                #print type(m.group())
                #if m.group(2) =

                mylist  = splitter.split(mystring)


                if mylist:
                    #if len(mylist) > 0:
                    for subtring in mylist:
                        print subtring

                    if all(len(substring) > minwordsize for substring in mylist):
                        print "**** possible number ****"
                        print

                        mlist = ['-'] * (len(mylist) * 2 - 1)
                        mlist[0::2] = mylist
                        output = m.group(1) + "".join(mlist).upper()
                        m1 = re.match(r'^(1)?(\d{3})?(\d+)',output)
                        if m1:
                            #print len(re.compile(m1).groups())
                            newlist = list()
                            #print m1.groups()
                            #print len(m1.groups())
                            for matches in m1.groups():
                                if matches:
                                    #print matches
                                    newlist.append(matches)
                                    newlist.append('-')
                            #print type(newlist)
                            output = "".join(newlist)+"".join(mlist).upper()
                            print m.group() + " ----> "+ output
                            print
                            #for  ):
                                #print i
                                #if not m1.group(i+1):
                                #    print "group(" + str(i+1) + "):  " + str(m1.group(i+1))
                                #print m1.groups(i)

                    #example = str(m.group()) + '\n'
                    #myfile.write(example
                #elif myset.issuperset(
            #example = "........" + str(m.group(2)) + '\n'
            #myfile.write(example)
            #print m.group()
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
        num_to_alphanum( input_list, index+1, output_list, size)

    if index is 0:
        myfile.seek(0)
        print "*****DONE*****"
        s = myfile.read()
        #print s
        # word = "DOI"
        # match = re.search(r'(\d+)' + word, s)
        # if match:
        #     print "Match found!"
        #     print match.group()
        myfile.close()
    return


for i in range(10):
    print "index:" + str(i)
    mytuple = const_hashTable[str(i)]
    #print mytuple
    #print "len = " + str(len(mytuple))
    for j in range(len(const_hashTable[str(i)])):
        print const_hashTable[str(i)][j]

def isEnglish(  ):
    # word bank source from:
    # https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
    # http://www-personal.umich.edu/~jlawler/wordlist
    # https://stackoverflow.com/questions/17426426/python-re-find-a-specific-word-in-a-text-document
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    absolute_path_2_file = os.path.join(THIS_FOLDER, 'wordlist.txt')
    myfile = open(absolute_path_2_file, "r")

    # regex = "(\d+)" + word + "\\b"
    # print regex
    # pattern = re.compile(regex,  re.IGNORECASE)
    # print pattern
    # match = re.search(pattern, alphanum_string)
    # if match:
    #     print "Match found!"
    #     print match.group()

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    absolute_path_2_file = os.path.join(THIS_FOLDER, 'output.txt')
    print "*****search for enlgish words*******"
    with open(absolute_path_2_file, "r") as alphafile:
        # get english word fromalphabetize list
        for line in alphafile:
            words = line.split()
            try:
                alphanum = words[0]
                alpha = re.sub(r'\d', "", alphanum)
                #print alpha
                if len(alpha) > 1:
                    if isEnlish.check(alpha):
                        print "Match found!"
                        print alphanum
                        print len(alpha)
            except IndexError:
                return 0


    #print str(type(outputread))
    #print str(my_regex)
    mystring = myfile.read()
    print mystring
    matches = re.match(r'(1800DOG)', mystring)
    if matches:
        print "Match found!"
        #print matches.group()


def maybe( string, myset):

    # word = "foi"
    i = 0
        # regex = "(\d+)" + word + "\\b"
        # print regex
        # pattern = re.compile(regex,  re.IGNORECASE)
    print "in string : " + string

    if isEnlglish.check( string):
        print string + " is an english word"
        myset.add( string )
        return 1, myset

    for word in lines:
        i += 1
        try:
            # match
            #print word
            #   (anything)(previously discoverd word)
            m = re.search("(\w+)(" + word+ ")\\b" , string)
            if m:
                #print "GOAL"
                #print "this.... "+ m.group()
                #print m.group(1)
                #print m.group(2)
                #if isEnglish.check(m.group(1)):
                    #example = str(m.group(2)) + '\n'
                    #myfile.write(example)
                    print word

        except:
            continue




def func_caller( phone_number ):
    print "Phone_number: " + phone_number
    # Remove anything other than digits
    cleaned_number = re.sub(r'\D', "", phone_number)
    print "Phone Num : ", cleaned_number
    number = list(cleaned_number)
    size = len(number)
    result = range(size)
    num_to_alphanum(number, 0, result, size )
    return
# 7246837
# 1-800-7246827
#
# 535537263535537

# catdogfish
# 2283643474

# coolpets
# 26657387

print splitter.split("painter")
print splitter.split("dog")



#
some_number = "7246837"
func_caller( some_number )

this = splitter.split("1800S246837")
print "".join(this)
if this:
    print "".join(this)
    #for splits in this:
    ##print splits
    mlist = ['-'] * (len(this) * 2 - 1)
    mlist[0::2] = this
    print "".join(mlist)
#print splitter.split("dog")
