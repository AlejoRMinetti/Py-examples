# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    shifteada = chr(ord(letter)+n)
    if ord(shifteada) > ord('z'):
        return chr(ord(shifteada)-(ord('z')-ord('a')+1))
    elif ord(shifteada) < ord('a'):
        return chr(ord(shifteada)+(ord('z')-ord('a')+1))
    else:
        return shifteada

def rotate(cadenita, n):
    # Your code here
    newChain = ""
    for char in cadenita:
        if char == " ":
            newChain += " "
        else:
            newChain += shift_n_letters(char, n)
    return newChain

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???