def palidrom(word):
    """
    Funkcja odwraca słowo i sprawdza czy jest takie samo jak pierwotnie podane
    """
    normal = word[::]
    reverse = word[::-1]
    if normal == reverse:
        return True 
    else:
        return False

result = palidrom('kaja')
print(result)