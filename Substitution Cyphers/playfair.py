#TODO:
#  zip in the for is wrong
#   Upper e lower no if da linha 27
#  the rest

def play_fair(plaintext, cypher):
    
    new_alphabet = cypher.lower()
    abc = "abcdefghiklmnopqrstuvwxyz"
    for letter in abc:
        if letter not in new_alphabet:
            new_alphabet += letter
    
    cyphertext = ""

    i=0
    for char1, char2 in zip(plaintext, plaintext[1:]):#ERRADO
        if char1.lower() == char2.lower():
            if char1.islower():
                cyphertext += 'x'
            else:
                cyphertext += 'X'
            if char2.islower():
                cyphertext += 'x'
            else:
                cyphertext += 'X'
        if abc.index(char1)//5 == abc.index(char2)//5:
            if abc.index(char1)%5==4:
                cyphertext += (abc.index(char1)//5)*5
            else:
                cyphertext += abc.index(char1)+1
            if abc.index(char2)%5==4:
                cyphertext += (abc.index(char2)//5)*5
            else:
                cyphertext += abc.index(char2)+1
        


if __name__ == "__main__":
    play_fair("damiao")