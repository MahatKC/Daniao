import numpy as np

def rail_fence(plaintext, n):
    if type(n) != int: raise  NameError("Expected integer as parameter")
    if n == 0: raise ZeroDivisionError

    plaintext_length = len(plaintext)
    line_size = int(np.ceil(plaintext_length/n))
    cyphertext = ""

    for i in range(n):
        for j in range(line_size):
            if j*n+i<plaintext_length:
                cyphertext+=plaintext[j*n+i]

    return cyphertext

if __name__ == "__main__":
    try:
        rail_fence("meetmeafterthetogaparty","a")
    except ZeroDivisionError:
        print("ok")
    except NameError:
        print("pikachu")
        