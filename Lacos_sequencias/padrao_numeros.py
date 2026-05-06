def number_pattern(n):
    if isinstance(n, int) == False:
        return 'Argument must be an integer value.'
    elif isinstance(n, int) == True and n < 1:
        return 'Argument must be an integer greater than 0.'

    ordens = []

    for n in range(1, n+1):
        ordens.append(str(n))

    
    return ' '.join(ordens)



print(number_pattern(4))
