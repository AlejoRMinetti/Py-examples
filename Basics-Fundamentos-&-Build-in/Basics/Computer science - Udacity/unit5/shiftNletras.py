# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    shifteada = chr(ord(letter)+n)
    if ord(shifteada) > ord('z'):
        return chr(ord(shifteada)-(ord('z')-ord('a')+1))
    elif ord(shifteada) < ord('a'):
        return chr(ord(shifteada)+(ord('z')-ord('a')+1))
    else:
        return shifteada

print shift_n_letters('z', 1)
#>>> a
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i