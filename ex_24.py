def main():
    global num
    num=int(input('Digite um número: '))
    if num==0 or num==1 or num==-1:
        print('Sem ser 1, -1 ou 0.')
        quit()
    check()
def check():
    global num
    if num%2==0:
        print('O número é divisível por 2.')
    else:
        print('O número não é divisível por 2.')
    if num%3==0:
        print('O número é divisível por 3.')
    else:
        print('O número não é divisível por 3.')
if(__name__=='__main__'):
     main()