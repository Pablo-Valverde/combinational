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
        return __combinate(characters, depth, prefix, func)

def __combinate(characters, depth = 5, prefix = "", func = print, iterations = 0):
        for c in characters:
                prefix += c
                func(prefix)
                if depth > 1:
                        iterations = __combinate(characters, depth - 1 , prefix, func, iterations)
                prefix = prefix[:-1]
        return iterations

#----Auxiliar -> to another proyect----#

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

with open("D:\Programs\hash\hashes.txt", "w") as file:
        pass

print(combinate(generate_comb(' ', '~'), 5, func=hash))
write()