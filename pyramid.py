# define a function with one parameter 
def pattern(n):
    k = 1
    while k < n:
        print( ' ' + (n-k) + '* ' * k)
        k += n
    k = n
    while k >= 1:
        print(' ' * (n-k) + '* ' * k)
        k -= 1

pattern(10)