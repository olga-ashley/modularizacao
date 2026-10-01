def diff():
    global a
    global b
    if a>b :
        d=a-b
        print('A é maior que B, e a diferença é igual a '+ str(d) +'.')
    else:
        d=b-a
        print('B é maior que A, e a diferença é igual a '+ str(d) +'.')
def main():
    global a
    global b
    a=int(input('Insira o valor A: '))
    b=int(input('Insira o valor B: '))
    if a==b:
        print('A e B são iguais.')
    else:
        diff()
main()
if(__name__=='__main__'):
     main()