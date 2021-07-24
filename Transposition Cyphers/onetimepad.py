def modulo_sum(x,y):
    return (x+y)%26

def alphabet_position(char):
    return ord(char.lower())-97

def character_sum(a,b):
    new_char_index = modulo_sum(alphabet_position(a),alphabet_position(b))
    return chr(new_char_index+97)

def one_time_pad(plaintext, cypher):
    cyphertext = "".join([character_sum(plaintext[i],cypher[i%len(cypher)]) for i in range(len(plaintext))])
    return cyphertext

if __name__ == "__main__":
    x=one_time_pad("hermes",2)
    print(x)