def alfabet():
    alfabet = ''
    for litera in range(65,91,1):
        litera = chr(litera)
        alfabet += litera
        
    return alfabet

def alfabet_cesara(przejscie):
    alfabet_cesara = ''
    poczatek = ''
    for litera in range(91-przejscie, 91, 1):
        poczatek += chr(litera)
    

    for litera in range(65,91 - przejscie ,1):
         litera = chr(litera)
         alfabet_cesara += litera

    return poczatek + alfabet_cesara

def szyfruj(text, przejscie):
    haslo = ''
    for litera in text.upper():
        litera = ord(litera) + przejscie
        if litera >= 91:
            litera = 'A'
            haslo += litera
        
        elif litera == 33:
            litera = ' '
            haslo += litera

        else:
            litera = chr(litera)
            haslo += litera
    
    return haslo


def deszyfruj(text, przejscie):
    haslo = ''
    for litera in text.upper():
        litera = ord(litera) - przejscie
        if litera == 64:
            litera = 'Z'
            haslo += litera
        
        elif litera == 31:
            litera = ' '
            haslo += litera

        else:
            litera = chr(litera)
            haslo += litera
    
    return haslo

print(alfabet())
print(alfabet_cesara(1))
print(szyfruj('ENIGMA',1))
print(deszyfruj(szyfruj('ENIGMA',1), 1))
