#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).
cache={}
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
        
    if cache.get(n-1):
        fiboMenosUno = cache[n-1]
    else:
        fiboMenosUno = fibonacci(n-1)
        cache[n-1] = fiboMenosUno
    if cache.get(n-2):
        fiboMenosDos = cache[n-2]
    else:
        fiboMenosDos = fibonacci(n-2)
        cache[n-2] = fiboMenosDos
    return fiboMenosUno + fiboMenosDos



print fibonacci(36)
#>>> 14930352
print fibonacci(500)
#>>> 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125