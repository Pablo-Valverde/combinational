def generate_comb(cfrom, cto):
        charlist = []
        for dec in range(ord(cfrom), ord(cto)+1):
                charlist.append(chr(dec))
        return charlist

def calc_iterations(characters, depth):
        result = 0
        for x in range(1, depth + 1):
                result += pow(characters.__len__(), x)
        return result

def combinate(characters, depth = 5, prefix = "", func = print):
        total_iterations = calc_iterations(characters, depth)
        __combinate(characters, depth, prefix, func)
        return total_iterations

def __combinate(characters, depth = 5, prefix = "", func = print):
        for c in characters:
                prefix += c
                func(prefix)
                if depth > 1:
                        __combinate(characters, depth - 1 , prefix, func)
                prefix = prefix[:-c.__len__()]

#----Auxiliar -> to another proyect----#

#----Dict combinate----#

import _thread
from os import close

__keywords = set()
__buffer = ""
file = open("E:\Programs\\test\contras.txt", "w")

def addword(word):
        split = word
        ind = 0
        offset = split.__len__()-1
        while split.__len__() != 0:
                __keywords.add(split)
                if (ind + offset) > word.__len__():
                        ind = 0
                        offset -= 1
                split = word[ind:ind + offset]
                ind += 1

def addwords(words):
        for word in words:
                addword(word)

def func(comb):
        global __buffer
        __buffer += comb + "\n"
        if __buffer.split("\n").__len__() > 10000:
                _thread.start_new_thread(writeb, ())

def writeb():
        global __buffer
        file.write(__buffer)
        __buffer = ""

#----Hash paswords----#

import hashlib

__hashes = {}

def matches(c):
        return (c >= ' ' and c <= '/') or (c >= ':' and c <= '~')

def format(s):
        sformated = ""
        for c in s:
                if not matches(c):
                        sformated += ord(c).__str__()
                else:
                        sformated += c
                sformated += '.'
        return sformated[:-1]

def hash(s):
        if __hashes.__len__() == 100000:
                write()
                __hashes.clear()
        __hashes[s] = format(sha256(s))

def write():
        buffer = ""
        for key in __hashes:
                buffer += key + ":" + __hashes[key] + "\n"
        with open("D:\Programs\hash\hashes.txt", "ab") as file:
                file.write(buffer.encode())

def sha256(s):
    und_hash = hashlib.sha256()
    und_hash.update(s.encode())
    dig_hash = und_hash.digest().decode("Latin1")
    return dig_hash

phrase = "sacarmela for the win madre 1 2 3 4 5 6 7 8 9 0"
addwords(phrase.split(" "))
combinate(__keywords, 4, func=func)
writeb()
file.close()