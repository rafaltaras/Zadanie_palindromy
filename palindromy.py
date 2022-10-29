
from cgi import print_directory


def palidrom(word):
    """
    Funkcja odwraca słowo i sprawdza czy jest takie samo jak pierwotnie podane
    """
    normal = word[::]
    reverse = word[::-1]
    if normal == reverse:
        print(f"Słowo {word} jest palidronem")
    else:
        print(f"Słowo {word} nie jest palidronem")

palidrom('meble')