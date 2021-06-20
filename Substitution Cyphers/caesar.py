def rot_n(plaintext,n):
    """Implementation of caesar cypher"""

    cyphertext = ""

    for character in plaintext:
        if character.islower():
            cyphertext += chr(((ord(character)-97+n)%26)+97)
        elif character.isupper():
            cyphertext += chr(((ord(character)-65+n)%26)+65)
        else:
            cyphertext += character

    return cyphertext

def ui():
    print("Insert the text to be encyphered")
    plaintext = input()
    print("Input the desired N for the ROT-N")
    n = int(input())

    return plaintext, n

if __name__ == "__main__":
    plaintext, n = ui()
    print(rot_n(plaintext, n))