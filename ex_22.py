def main():
    global numA
    global numB
    numA=int(input('Um valor: '))
    numB=int(input('Outro valor: '))
    calc()

    print(str(numA) + ',', str(numB)+'.')


def calc():
    global numA
    global numB
    if numA<numB:
        numA, numB = numB , numA
if(__name__=='__main__'):
     main()