tab = []
size = 10

def getNumber():
    x = int(input())
    if len(str(x)) > 4:
        print("Prosze podac liczbe jeszcze raz")
        x = getNumber()
    return x

def isAPrimeNumber(number):
    if number < 2:
        return False
    if number == 2:
        return True
    i = 2
    while i < number:
        if (number % i) == 0:
            return False
        i+=1
    return True

for i in range(size):
    x = getNumber()
    tab.append(x)
    
for i in range(size):
    if isAPrimeNumber(tab[i]):
        print(f'Liczba {i+1} jest liczba pierwsza')
        continue 
    print(f'Liczba {i+1} nie jest liczba pierwsza')


