def eliminate_spaces(string):
    return string.replace(" ","")

def cypher_creation(cypher):
    lowered_cypher = eliminate_spaces(cypher.lower())

    new_alphabet = ""
    for char in lowered_cypher:
        if char not in new_alphabet:
            new_alphabet += char
    abc = "abcdefghiklmnopqrstuvwxyz"
    for letter in abc:
      if letter not in new_alphabet:
        new_alphabet += letter
    
    return new_alphabet

def add_bogus_z(temp_plaintext):
    if len(temp_plaintext)%2 == 0:
        temp_plaintext += "z"

    return temp_plaintext

def tuple_creation(temp_plaintext):
    temp_plaintext_size = len(temp_plaintext)
    tuples = []
    i=0
    while i<temp_plaintext_size:
        if i+1 == temp_plaintext_size:
            new_tuple = (temp_plaintext[i], "z")
            i += 1
        elif temp_plaintext[i] == temp_plaintext[i+1]:
            new_tuple = (temp_plaintext[i], "x")
            i += 1
        else:
            new_tuple = (temp_plaintext[i], temp_plaintext[i+1])
            i += 2
        tuples.append(new_tuple)

    return tuples

def create_temp_plaintext(plaintext):
    temp_plaintext = plaintext.replace("j","i").lower()
    temp_plaintext = eliminate_spaces(temp_plaintext)
    temp_plaintext = add_bogus_z(temp_plaintext)

    return temp_plaintext

def check_uppercase_letters(plaintext, cyphertext):
    final_cyphertext = ""
    i = 0
    for character in plaintext:
        if character.isupper():
            final_cyphertext += cyphertext[i].upper()
            i += 1
        elif character.islower():
            final_cyphertext += cyphertext[i]
            i += 1
    final_cyphertext += cyphertext[i:]

    return final_cyphertext

def same_row(char1,char2,new_alphabet):
    return new_alphabet.index(char1)//5 == new_alphabet.index(char2)//5

def get_char_to_the_right(char1,new_alphabet):
    if new_alphabet.index(char1)%5 == 4:
        return new_alphabet[(new_alphabet.index(char1)//5)*5]
    else:
        return new_alphabet[new_alphabet.index(char1)+1]

def equal_chars(char1,char2):
    return char1.lower() == char2.lower()

def same_column(char1,char2,new_alphabet):
    return new_alphabet.index(char1)%5 == new_alphabet.index(char2)%5

def get_char_below(char1,new_alphabet):
    return new_alphabet[(new_alphabet.index(char1)+5)%25]

def get_char_a_in_same_column_as_b(char1,char2,new_alphabet):
    return new_alphabet[(new_alphabet.index(char1)//5)*5+(new_alphabet.index(char2)%5)]

def playfair_steps(tuples, new_alphabet):
    cyphertext=""
    
    for char1, char2 in tuples:
        if same_row(char1,char2,new_alphabet):
            cyphertext += get_char_to_the_right(char1,new_alphabet)
            cyphertext += get_char_to_the_right(char2,new_alphabet)  
        elif same_column(char1,char2,new_alphabet):
            cyphertext += get_char_below(char1,new_alphabet)
            cyphertext += get_char_below(char2,new_alphabet)
        else:
            cyphertext += get_char_a_in_same_column_as_b(char1,char2,new_alphabet)
            cyphertext += get_char_a_in_same_column_as_b(char2,char1,new_alphabet)
    
    return cyphertext

def play_fair(plaintext, cypher):
    new_alphabet = cypher_creation(cypher)
    temp_plaintext = create_temp_plaintext(plaintext)
    tuples = tuple_creation(temp_plaintext)
    cyphertext = playfair_steps(tuples,new_alphabet)
    final_cyphertext = check_uppercase_letters(plaintext, cyphertext)

    return final_cyphertext

if __name__ == "__main__":
    print(play_fair("Hide the gold in the tree stump","playfair example"))