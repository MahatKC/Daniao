def rot_char(character, n):
    """Rot-n for a single character"""
    if character.islower():
        return chr(((ord(character)-97+n)%26)+97)
    elif character.isupper():
        return chr(((ord(character)-65+n)%26)+65)
    else:
        return character

def rot_n(plaintext,n):
    """Implementation of caesar cypher"""

    cyphertext = ""

    for character in plaintext:
        cyphertext += rot_char(character, n)

    return cyphertext

def ui():
    """UI Implementation with prints and inputs"""
    print("Insert the text to be encyphered")
    plaintext = input()
    print("Input the desired N for the ROT-N")
    n = int(input())

    return plaintext, n

if __name__ == "__main__":
    plaintext, n = ui()
    print(rot_n(plaintext, n))