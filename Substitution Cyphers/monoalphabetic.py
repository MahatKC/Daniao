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

if __name__ == "__main__":
    print(monoalpha("heRMEs","wxyzAbcdefghijklmNOpqrstuv"))