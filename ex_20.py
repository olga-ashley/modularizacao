def main():
    global coA 
    global coB
    global delta
    coA=float(input('Digite o Coeficiente A: '))
    coB=float(input('Digite o Coeficiente B: '))
    coC=float(input('Digite o Coeficiente C: '))
    delta=(coB**2)-(4*coA*coC)
    if delta<0 :
        print('Não há raiz real.')
    else:
        raizes()

def raizes():
    global coA 
    global coB
    global delta
    raiz1=(-coB+(delta**0.5))/(2*coA)
    raiz2=(-coB-(delta**0.5))/(2*coA)
    if raiz1==raiz2:
        print('A única raiz é igual a', str(raiz2) +'.')
    else:
        print('A primeira raiz é igual a', str(raiz1) +'.')
        print('A segunda raiz é igual a', str(raiz2) +'.')
if(__name__=='__main__'):
     main()
