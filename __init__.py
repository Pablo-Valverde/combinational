__keywords = set()
__buffer = ""
filename = "YOUR FILE HERE"
file = open(filename, "w")

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
        print(total_iterations)
        __combinate(characters, depth, prefix, func)
        return total_iterations

def __combinate(characters, depth = 5, prefix = "", func = print):
        for c in characters:
                prefix += c
                func(prefix)
                if depth > 1:
                        __combinate(characters, depth - 1 , prefix, func)
                prefix = prefix[:-c.__len__()]

#----Dict combinate----#

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
                writeb()

def writeb():
        global __buffer
        file.write(__buffer)
        __buffer = ""
