from caesar import rot_char

def vigenere(plaintext,cypher):
    """Implementation of vigenere cypher"""
    
    i = 0
    cyphertext = ""
    for character in plaintext:
        n = ord(cypher[i%len(cypher)].lower())-97
        new_char = rot_char(character, n)
        cyphertext += new_char
        if new_char != ' ':
            i += 1
    return cyphertext

def ui():
    """UI Implementation with prints and inputs"""
    print("Insert the text to be encyphered")
    plaintext = input()
    print("Insert the cypher")
    cypher = input()

    return plaintext, cypher

if __name__ == "__main__":
    plaintext, cypher = ui()
    print(vigenere(plaintext, cypher))
    