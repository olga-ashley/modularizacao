def main():
    global numA, numB
    numA=int(input('Insira o valor A: '))
    numB=int(input('Insira o valor B: '))
    if numA<=0 or numB<=0:
        print('Não use um valor menor ou igual a 0.')
        quit()
    if numA>numB:
        divide()
    elif numB>numA:
        numA, numB = numB , numA
        divide()
    else:
        print('Os valores são iguais.')

        
def divide():
    global numA, numB
    if numA%numB==0:
        numB=str(numB)
        print(numA,'é maior que', numB+ '.', numA, 'é multiplo de', numB +'.')
    else:
        numB=str(numB)
        print(numA,'é maior que', numB+ '.', numA,'não é multiplo de', numB +'.')
if(__name__=='__main__'):
     main()