import random as r

def Obtener_ecuacion(grado=1, *args):
    if grado == 0: grado = r.randint(1, 3)

    if grado == 1:
        sym = r.choice(['+', '-'])
        num1 = r.randint(1, 30)
        num2 = r.randint(1, 30)
        
        if num1 < num2:
            num3 = num1 
            num1, num2 = num2, num3 

    elif grado == 2:
        sym = r.choice(['+', '-'])
        num1 = r.randint(10, 55)
        num2 = r.randint(10, 55) 

        if num1 < num2:
            num3 = num1 
            num1, num2 = num2, num3 

        num1 = int(f'{num1}00')
        num2 = int(f'{num2}00') 
        
    
    elif grado == 3:
        sym = r.choice(['+', '-', '*'])
        if sym == '*':    
            num1 = r.randint(1, 9)
            num2 = r.randint(1, 9)

        else:    
            num1 = r.randint(1, 1000)
            num2 = r.randint(1, 1000)

    else: return None

    if sym == '+': res = num1 + num2
    elif sym == '-': res = num1 - num2
    elif sym == '*': res = num1 * num2

    return [num1, sym, num2, res, f'{num1} {sym} {num2} = ?']

def Obtener_numeros(num_correct, *args):
    nums = [
        r.randint(num_correct-20, num_correct+20), 
        r.randint(num_correct-20, num_correct+20),
        r.randint(num_correct-20, num_correct+20),
        num_correct
    ]
    
    lista1 = nums.copy()
    lista2 = []
    __lista__ = []

    for x in range(0, len(nums), 1):
        n = r.choice(lista1)
        lista1.remove(n)
        lista2.append(n)

    for x in range(0, len(nums), 1):
        n = r.choice(lista2)
        lista2.remove(n)
        __lista__.append(n)
    
    return __lista__
    
#* Author: Francisco Velez
