def son_anagramas(palabra1, palabra2):
    if palabra1 == palabra2:
        return False


    if len(palabra1) != len(palabra2): 
        return False


    sorted_palabra1 = sorted(list(palabra1))
    sorted_palabra2 = sorted(list(palabra2))
    
    return sorted_palabra1 == sorted_palabra2


palabra1 = "el"
palabra2 = "le"
print("es una anagrama: ", son_anagramas(palabra1, palabra2))
palabra3 = "panthers"
palabra4 = "code"
print("es una anagrama: ", son_anagramas(palabra3, palabra4))
