from sortedcontainers import SortedDict
import numpy as np

def columnar(plaintext, cypher):
    if type(cypher) == int: raise  NameError("Expected not integer as parameter")

    sorted_dictionary = SortedDict()
    for key in cypher:
        sorted_dictionary[key] = ""
    cyphertext = ""

    n = len(cypher)
    if n == 0: raise ZeroDivisionError
    plaintext_length = len(plaintext)
    line_size = int(np.ceil(plaintext_length/n))

    for i in range(n):
        for j in range(line_size):
            if j*n+i<plaintext_length:
                sorted_dictionary[cypher[i]] += plaintext[j*n+i]

    for _,value in sorted_dictionary.items():
        cyphertext+= value

    return cyphertext    

if __name__ == "__main__":
    print(columnar("hermes", 1234))