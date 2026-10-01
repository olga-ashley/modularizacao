def fat(valF):
    totalfat=1
    while valF > 1:
        totalfat=valF*totalfat
        valF-=1
    return totalfat
def divser(numA, numB):
    totaldivser=1
    i=1
    while i <= numA:
        totaldivser=totaldivser+(1/eval(numB))
        i+=1
    return totaldivser

div = lambda valA,valB : valA/valB

def main():
    valA=int(input('Insira um valor A: '))
    valB=int(input('Insira um valor B: '))
    resAB= div(valA,valB)

    valN=int(input('Insira um valor N: '))
    resN=divser(valN, 'fat(i)')
    print('O valor da série 1+1/1!+...+1/'+str(valN)+'! é de', str(resN)+'.')
    print(valA,'dividido por',valB,'é igual a', str(resAB)+'.')
if(__name__=='__main__'):
     main()