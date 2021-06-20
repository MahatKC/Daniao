def monoalpha(plaintext, cypher):
    """Maps each plaintext char to its cypher correspodent"""
    cypher = cypher.lower()

    cyphertext = ""
    for character in plaintext:
        if character.islower():
            cyphertext += cypher[ord(character)-97].lower()
        elif character.isupper():
            cyphertext += cypher[ord(character)-65].upper()
        else:
            cyphertext += character
    
    return cyphertext

def ui():
    """UI Implementation with prints and inputs"""
    print("Insert the text to be encyphered")
    plaintext = input()
    print("Insert the randomized alphabet")
    cypher = input()

    return plaintext, cypher

if __name__ == "__main__":
    plaintext, cypher = ui()
    print(monoalpha(plaintext, cypher))