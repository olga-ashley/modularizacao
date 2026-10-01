def main():
    global numA
    global numB
    global numC
    global numX    
    numA=float(input('Insira o valor A: '))
    numB=float(input('Insira o valor B: '))
    numC=float(input('insira o valor C: '))
    numX=float(input('Insira o valor X: '))
    if numA>numB or numB>numC:
        print('A, B e C devem ser sequenciais.')
        quit()
    sort()
    print(str(numA)+',',str(numB)+',',str(numC)+',',str(numX)+'.')

def sort():
    global numA
    global numB
    global numC
    global numX 
    if numX<numA:
        numA, numB, numC, numX = numX, numA, numB, numC

    elif numX<numB:
        numA, numB, numC, numX = numA, numX, numB, numC

    elif numX<numC:
        numA, numB, numC, numX = numA, numB, numX, numC
if(__name__=='__main__'):
     main()