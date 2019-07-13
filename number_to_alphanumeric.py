#!/usr/bin/python
import time

def number_to_alphanumeric ( string ):
    # do something
    mylist = list(string)
    size = len(mylist)
    a = [0, 0]
    i = size-1
    # print("size" + str(i))
    flag = 0
    print "".join(mylist)
    while i >= 0:
        #print i
        mylist, flag = cycle(mylist, i)
        if flag == 0:
            if i != size - 1:
                i = size -1
            test = isNumAlpha(mylist, size)
            if test is not None:
                if test is 1:
                    time.sleep(.5)
                    index =  getAlpaIndex( mylist )
                    print "".join(mylist)
                    print "".join(mylist[index:])
            continue;
        else:
            i = i - 1
        continue

def cycle(mylist, int):
    flag = 0
    #print "cycling element " + str(int) + " of list \"" + str(mylist) + "\""
    if mylist[int] == '1':
        mylist, flag = cycle_1(mylist, int)
    if mylist[int] == '0':
        mylist, flag = cycle_0(mylist, int)
    elif mylist[int] == '2' or mylist[int] == 'A' or mylist[int] == 'B' or mylist[int] == 'C':
        mylist, flag = cycle_2(mylist, int)
    elif mylist[int] == '3' or mylist[int] == 'D' or mylist[int] == 'E' or mylist[int] == 'F':
        mylist, flag = cycle_3(mylist, int)
    elif mylist[int] == '4' or mylist[int] == 'G' or mylist[int] == 'H' or mylist[int] == 'I':
        mylist, flag = cycle_4(mylist, int)
    elif mylist[int] == '5' or mylist[int] == 'J' or mylist[int] == 'K' or mylist[int] == 'L':
        mylist, flag = cycle_5(mylist, int)
    elif mylist[int] == '6' or mylist[int] == 'M' or mylist[int] == 'N' or mylist[int] == 'O':
        mylist, flag = cycle_6(mylist, int)
    elif mylist[int] == '7' or mylist[int] == 'P' or mylist[int] == 'Q' or mylist[int] == 'R' or mylist[int] == 'S':
        mylist, flag = cycle_7(mylist, int)
    elif mylist[int] == '8' or mylist[int] == 'T' or mylist[int] == 'U' or mylist[int] == 'V':
            mylist, flag = cycle_8(mylist, int)
    elif mylist[int] == '9' or mylist[int] == 'W' or mylist[int] == 'X' or mylist[int] == 'Y' or mylist[int] == 'Z':
        mylist, flag = cycle_9(mylist, int)

    #print "returning list = " + "".join(mylist)
    return mylist, flag

def cycle_0 ( mylist, int):
    return mylist, 1

def cycle_1 ( mylist, int ):
    # 1 has no alpha rules
    # pivot to next element
    return mylist, 1

def cycle_2 ( mylist, int ):
    # 2 could be 'A' 'B' 'C'
    if mylist[int] == "2":
        mylist[int] = "A"
        return mylist, 0
    elif mylist[int] == "A":
        mylist[int] = "B"
        return mylist, 0
    elif mylist[int] == "B":
        mylist[int] = "C"
        return mylist, 0
    elif mylist[int] == "C":
        mylist[int] = "2"
        return mylist, 1

def cycle_3 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "3":
        mylist[int] = "D"
        return mylist, 0
    elif mylist[int] == "D":
        mylist[int] = "E"
        return mylist, 0
    elif mylist[int] == "E":
        mylist[int] = "F"
        return mylist, 0
    elif mylist[int] == "F":
        mylist[int] = "3"
        return mylist, 1

def cycle_4 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "4":
        mylist[int] = "G"
        return mylist, 0
    elif mylist[int] == "G":
        mylist[int] = "H"
        return mylist, 0
    elif mylist[int] == "H":
        mylist[int] = "I"
        return mylist, 0
    elif mylist[int] == "I":
        mylist[int] = "4"
        return mylist, 1

def cycle_5 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "5":
        mylist[int] = "J"
        return mylist, 0
    elif mylist[int] == "J":
        mylist[int] = "K"
        return mylist, 0
    elif mylist[int] == "K":
        mylist[int] = "L"
        return mylist, 0
    elif mylist[int] == "L":
        mylist[int] = "5"
        return mylist, 1

def cycle_6 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "6":
        mylist[int] = "M"
        return mylist, 0
    elif mylist[int] == "M":
        mylist[int] = "N"
        return mylist, 0
    elif mylist[int] == "N":
        mylist[int] = "O"
        return mylist, 0
    elif mylist[int] == "O":
        mylist[int] = "6"
        return mylist, 1

def cycle_7 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "7":
        mylist[int] = "P"
        return mylist, 0
    elif mylist[int] == "P":
        mylist[int] = "Q"
        return mylist, 0
    elif mylist[int] == "Q":
        mylist[int] = "R"
        return mylist, 0
    elif mylist[int] == "R":
        mylist[int] = "S"
        return mylist, 0
    elif mylist[int] == "S":
        mylist[int] = "R"
        return mylist, 1

def cycle_8 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "8":
        mylist[int] = "T"
        return mylist, 0
    elif mylist[int] == "T":
        mylist[int] = "U"
        return mylist, 0
    elif mylist[int] == "U":
        mylist[int] = "V"
        return mylist, 0
    elif mylist[int] == "V":
        mylist[int] = "T"
        return mylist, 1

def cycle_9 ( mylist, int ):
    # 3 could be 'D' 'E' 'F'
    if mylist[int] == "9":
        mylist[int] = "W"
        return mylist, 0
    elif mylist[int] == "W":
        mylist[int] = "X"
        return mylist, 0
    elif mylist[int] == "X":
        mylist[int] = "Y"
        return mylist, 0
    elif mylist[int] == "Y":
        mylist[int] = "Z"
        return mylist, 0
    elif mylist[int] == "Z":
        mylist[int] = "W"
        return mylist, 1

def isNumAlpha ( mylist, size ):
    # test formating for [ list_of_numbers , list_of_characters ]
    # example [ 1 3 2 4 a c b d ] returns 1
    mystring = "".join(mylist)
    i = 0
    if mystring[i].isalpha() is False:
        # branch1 results 1,2,3,A,B,B or 1,2,3
        i += 1
        while i < size - 1:
            if mystring[i].isalpha() is False:
                # still catching numbers
                i += 1
                continue
            else:
                # caught a character
                i += 1
                while i < size - 1:
                    if mystring[i].isalpha() is False:
                        # caught number after character
                        return 0
                    else:
                        i +=1
                return 1
    elif mystring[i].isalpha() is not False:
        # brancn2 A,B,C ( no numbers)
        i += 1
        while i < size - 1:
             if mystring[i].isalpha() is False:
                 # caught number after character
                 return 0
             else:
                 i +=1;
        return 1
    else:
        return 0

def getAlpaIndex( mylist ):
    mystring = "".join(mylist)
    i = 0
    for char in mystring:
        if char.isalpha() is not False:
            return i
        else:
            i += 1
    return i



text = "222"
mylist = list(text)
mylist[2]= "A"
size = len(mylist)
text = "".join(mylist)
print "size of \"" + text + "\" is "  + str(size)

text = "7246837"
number_to_alphanumeric(text)
